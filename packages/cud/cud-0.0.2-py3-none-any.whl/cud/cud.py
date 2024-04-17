"""
Copyright 2024 David Woodburn

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
--------------------------------------------------------------------------------
"""

__author__ = "David Woodburn"
__license__ = "MIT"
__date__ = "2024-04-15"
__maintainer__ = "David Woodburn"
__email__ = "david.woodburn@icloud.com"
__status__ = "Development"

import math
import numpy as np
import scipy as sc


class Set:
    def __init__(self, t, y, tref=None, rate_jumps=False):
        self.t0 = t.copy()
        self.y0 = y.copy()
        self.t = t.copy()
        self.y = y.copy()
        self.t_ref = tref
        self.rate_jumps = rate_jumps      # tolerance on diff spikes


class Group:
    def __init__(self, tol=1e-2, default=None):
        self.sets = []  # list of data sets
        self.tol = tol  # time step tolerance factor
        self.repeats = True     # flag to replace repeat values
        self.default = default  # value to treat as blank

    def add(self, t, y, tref=0, rate_jumps=False):
        s = Set(t, y, tref, rate_jumps)
        self.sets.append(s)

    def overlay(self, method="cubic"):
        # Adjust time arrays for varying reference times.
        adjust_time(self.sets)

        # Correct irregular time step sizes.
        dt_min = correct_time_steps(self.sets, self.tol)

        # Delete values to be treated as blanks.
        if self.default is not None:
            replace_default_values(self.sets, self.default)

        # Replace points which are repeat previous values.
        if self.repeats:
            replace_repeats(self.sets)

        # Fix spikes.
        fix_spikes(self.sets)

        # Resample the sets using a uniform sampling rate for all sets,
        # over the same domain.
        resample_uniformally(self.sets, dt_min)

    def clip(self, t_min, t_max):
        J = len(self.sets)
        for j in range(J):
            t = self.sets[j].t
            y = self.sets[j].y
            na = np.sum(t <= t_min)
            nb = np.sum(t <= t_max)
            self.sets[j].t = t[na:nb]
            if y.ndim == 1:
                self.sets[j].y = y[na:nb]
            else:
                self.sets[j].y = y[:, na:nb]

            # FIXME Remove
            t = self.sets[j].t0
            y = self.sets[j].y0
            na = np.sum(t <= t_min)
            nb = np.sum(t <= t_max)
            self.sets[j].t0 = t[na:nb]
            if y.ndim == 1:
                self.sets[j].y0 = y[na:nb]
            else:
                self.sets[j].y0 = y[:, na:nb]


def adjust_time(sets):
    # Check the absolute time references.
    t_ref_min = math.inf
    J = len(sets)
    for j in range(J):
        t_ref = sets[j].t_ref
        if t_ref is None:
            continue
        if t_ref_min is None or t_ref < t_ref_min:
            t_ref_min = t_ref

    # Adjust time arrays.
    if t_ref_min is not None:
        for j in range(J):
            t_ref = sets[j].t_ref
            del_t = t_ref - t_ref_min
            sets[j].t += del_t


def fix_spikes(sets):
    def find_spikes(t, y):
        Dy = np.diff(y)/np.diff(t)
        Dya = Dy[:-1]
        Dyb = Dy[1:]
        mm = np.where(Dya*Dyb < 0)[0]
        m_tol = int(len(mm)*0.999)
        tol = np.sort(np.sqrt(-Dya[mm]*Dyb[mm]))[m_tol]
        n_up = np.where((Dya > tol) & (Dyb < -tol))[0] + 1
        n_dn = np.where((Dya < -tol) & (Dyb > tol))[0] + 1
        nn = np.concatenate((n_up, n_dn))
        return nn

    def fix_set_spikes(t, y):
        ts = t.copy()
        ys = y.copy()
        nn = find_spikes(ts, ys)
        while len(nn) > 0:
            ys = np.delete(ys, nn)
            ts = np.delete(ts, nn)
            nn = find_spikes(ts, ys)
        if len(ts) < len(t):
            ys = np.interp(t, ts, ys)
        return ys

    for j in range(len(sets)):
        # Get the data for this set.
        t = sets[j].t
        Y = sets[j].y
        rate_jumps = sets[j].rate_jumps

        if rate_jumps == False:
            continue

        if Y.ndim == 1:
            dt = np.diff(t)
            Dy = np.diff(Y)/dt
            Dy = fix_set_spikes(t[:-1], Dy)
            Y[1:] = Y[0] + np.cumsum(Dy)*dt
        else:
            for row in range(Y.shape[0]):
                y = Y[row]
                dt = np.diff(t)
                Dy = np.diff(y)/dt
                Dy = fix_set_spikes(t[:-1], Dy)
                y[1:] = y[0] + np.cumsum(Dy*dt)
                Y[row] = y.copy()

        sets[j].y = Y


def correct_time_steps(sets, tol):
    J = len(sets)
    dt_min = math.inf
    for j in range(J):
        # Get the time array for this set.
        t = sets[j].t

        # Save the mid time value.
        t_mid0 = (t[-1] + t[0])/2

        # Find the median time step.
        dt = np.diff(t)
        dt_median = np.median(dt)

        # Find the mean of the "normal" steps.
        dt_lo = dt_median*(1 - tol)
        dt_hi = dt_median*(1 + tol)
        is_normal = (dt >= dt_lo)*(dt <= dt_hi)
        nn_normal = np.where(is_normal)[0]
        dt_mean = np.mean(dt[nn_normal])

        # Replace the time steps with multiples of nice time steps.
        dt = np.round(dt/dt_mean)*dt_mean

        # Integrate the time steps to produce a new time array.
        t[1:] = t[0] + np.cumsum(dt)

        # Get the new mid time value and adjust to match the old.
        t_mid = (t[-1] + t[0])/2
        t -= t_mid - t_mid0

        # Store the new time array.
        sets[j].t = t

        # Keep track of the smallest mean time step.
        if dt_mean < dt_min:
            dt_min = dt_mean

    return dt_min


def replace_default_values(sets, default):
    for j in range(len(sets)):
        Y = sets[j].y
        if Y.ndim == 1: # 1D
            nn_nans = np.where(Y == default)[0]
            if len(nn_nans) > 0:
                Y = replace_values(Y, nn_nans)
        else: # 2D
            for row in range(Y.shape[0]):
                nn_nans = np.where(Y[row, :] == default)[0]
                if len(nn_nans) > 0:
                    Y[row, :] = replace_values(Y[row, :], nn_nans)
        sets[j].y = Y


def replace_values(y, nn_replace):
    # Find the edges of the regions of repeat values.
    dnn_repeats = np.diff(nn_replace)
    mm_jumps = np.where(dnn_repeats > 1)[0]
    nn_first = nn_replace[0] - 1
    nn_starts = nn_replace[mm_jumps + 1] - 1
    nn_stops = nn_replace[mm_jumps] + 1
    nn_last = nn_replace[-1] + 1
    if nn_last >= len(y):
        nn_last = len(y) - 1
    nn_edges = np.concatenate(([nn_first], nn_starts,
            nn_stops, [nn_last]))
    nn_edges = np.unique(np.sort(nn_edges))

    # Reinterpolate the repeat values.
    #y[nn_replace] = sc.interpolate.CubicSpline(
    #        nn_edges, y[nn_edges])(nn_replace)
    y[nn_replace] = sc.interpolate.pchip_interpolate(
            nn_edges, y[nn_edges], nn_replace)
    return y


def replace_repeats(sets):
    def replace_repeats_1D(y):
        # Find where y repeats values.
        dy = np.diff(y)
        nn_repeats = np.where(dy == 0)[0] + 1
        if len(nn_repeats) == 0:
            return y
        return replace_values(y, nn_repeats)

    # For each set, process the y data.
    for j in range(len(sets)):
        if sets[j].y.ndim == 1: # 1D
            sets[j].y = replace_repeats_1D(sets[j].y)
        else: # 2D
            Y = sets[j].y
            for row in range(Y.shape[0]):
                y = replace_repeats_1D(Y[row, :])
                Y[row, :] = y
            sets[j].y = Y


def resample_uniformally(sets, dt_min):
    # Get the minimum and maximum times.
    t_min = -math.inf
    t_max = math.inf
    t_anchor = 0.0
    for j in range(len(sets)):
        # Expand the group min and max.
        t = sets[j].t
        t_min_j = np.nanmin(t)
        t_max_j = np.nanmax(t)
        if t_min_j > t_min:
            t_min = t_min_j
        if t_max_j < t_max:
            t_max = t_max_j

        # If this data set is the max frequency,
        # save the midpoint as an anchor.
        dt_median = np.median(np.diff(t))
        if np.abs(dt_median - dt_min) < dt_min/10:
            t_anchor = t[len(t)//2]
    if t_max <= t_min:
        raise ValueError("There is no single overlap for the data sets.")

    # Create a new time array with the minimum sampling rate.
    t_min = t_anchor - round((t_anchor - t_min)/dt_min)*dt_min
    t_max = t_anchor + round((t_max - t_anchor)/dt_min)*dt_min
    K = round((t_max - t_min)/dt_min) + 1
    tt = np.linspace(t_min, t_max, K)

    # Reinterpolate each set with the new time array.
    for j in range(len(sets)):
        t = sets[j].t
        y = sets[j].y
        #y = sc.interpolate.CubicSpline(t, y, axis=1)(tt)
        y = sc.interpolate.pchip_interpolate(t, y, tt, axis=1)
        sets[j].t = tt.copy()
        sets[j].y = y
