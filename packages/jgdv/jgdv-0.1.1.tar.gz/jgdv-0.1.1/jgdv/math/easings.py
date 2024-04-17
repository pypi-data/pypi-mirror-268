"""
Module of different easing functions
All functions take xs from -1 - 1,
and produce ys from 0 - 1
"""
##-- imports
from __future__ import annotations

from enum import Enum
import numpy as np
from .constants import PI

##-- end imports

CODOMAIN = Enum("Codomain of the curve", "FULL LEFT RIGHT")

def quantize(xs, r=None, q=5, bins=None):
    """ Given an array of numbers, quantize into a number of bins """
    if r is None:
        r = [xs.min(), xs.max()]
    if bins is None:
        bins = np.linspace(r[0], r[1], q)
    inds = np.digitize(xs, bins, right=True)
    return np.array([bins[x] for x in inds])

def interp(xs, r=None, codomain_e=CODOMAIN.FULL):
    """ Auto interpolate input to an -1 to 1 scale,
    r can override the calculated input domain of xs.min/max"""
    codomain = [-1, 1]
    if codomain_e == CODOMAIN.LEFT:
        codomain = [-1, 0]
    elif codomain_e == CODOMAIN.RIGHT:
        codomain = [0, 1]
    if r is None:
        r = [xs.min(), xs.max()]
    return np.interp(xs, r, codomain)

def pow_abs_curve(xs, a, r=None, codomain_e=CODOMAIN.FULL):
    """ 1 - pow(abs(x), a)
    Var a changes the curve.
    0.5: exp tri
    3.5: saturated bell """
    assert(0.5 <= a <= 3.5)
    ixs = interp(xs, r=r, codomain_e=codomain_e)
    return 1 - pow(np.abs(ixs), a)

def pow_cos_pi(xs, a, r=None, codomain_e=CODOMAIN.FULL):
    """ pow(cos(pi * x / 2) a)
    Var a changes curve
    0.5: semi circle
    3.5: gaussian window """
    assert(0.5 <= a <= 3.5)
    ixs = interp(xs, r=r, codomain_e=codomain_e)
    return pow(np.cos(PI * ixs * 0.5), a)

def pow_abs_sin_pi(xs, a, r=None, codomain_e=CODOMAIN.FULL):
    """ 1 - pow(abs(sin(pi * x / 2)), a)
    Var a changes curve
    0.5: exp_tri
    3.5: slightly saturated f
    """
    assert(0.5 <= a <= 3.5)
    ixs = interp(xs, r=r, codomain_e=codomain_e)
    return 1 - pow(np.abs(np.sin(PI * ixs * 0.5)), a)

def pow_min_cos_pi(xs, a, r=None, codomain_e=CODOMAIN.FULL):
    """ 1 - pow(min(cos(pi * x / 2), 1 - abs(x)), a)
    Var a changes curve
    0.5: leaf
    3.5: ep_tri
    """
    assert(0.5 <= a <= 3.5)
    ixs = interp(xs, r=r, codomain_e=codomain_e)
    ixs_balanced = np.column_stack((np.cos(PI * ixs * 0.5), 1 - np.abs(ixs)))
    return 1 - pow(np.min(ixs_balanced, axis=1), a)

def pow_max_abs(xs, a, r=None, codomain_e=CODOMAIN.FULL):
    """ 1 - pow(max(0, abs(x)) * 2 - 1, a)
    Var a changes curve
    0.5: exp_tri
    3.5: slightly saturated f
    """
    assert(0.5 <= a <= 3.5)
    ixs = interp(xs, r=r, codomain_e=codomain_e)
    ixs_zero = np.column_stack((np.abs(ixs) * 2 - 1, np.zeros(len(ixs))))
    return 1 - pow(np.max(ixs_zero, axis=1), a)

def sigmoid(xs, a, r=None, codomain_e=CODOMAIN.FULL):
    """ 1 / (1 + e^(-5 * x)
    Var a does nothing
    """
    ixs = interp(xs, r=r, codomain_e=codomain_e)
    return 1 / (1 + pow(np.e, -5 * ixs))

def linear(xs, a, r=None, codomain_e=CODOMAIN.FULL):
    """ A linear easing: x = y """
    ixs = interp(xs, r=r, codomain_e=codomain_e)
    return ixs

def static(xs, a, r=None, codomain_e=CODOMAIN.FULL):
    """ No matter the values passed in return an array of 1's """
    return np.ones(xs.shape)

def soft_knee(i, threshold, ratio, knee):
    # A Simple soft_knee compression curve
    # Source: https://se.mathworks.com/help/audio/ref/compressor-class.html
    # Input: np.array, Threshold, Ratio, Knee width
    kneeStart, kneeEnd = (threshold - knee/2, threshold + knee/2)
    under              = i < kneeStart
    over               = kneeEnd < i
    inKnee             = np.invert(under) * np.invert(over)

    k_f              = (1/ratio - 1)
    intermediate     = (i - kneeEnd)
    intermediate_pow = pow(intermediate,2)
    k_div_amnt       = 2 * knee
    k_mod            = (k_f * intermediate_pow) / k_div_amnt
    k_red            = i + k_mod

    over_red = threshold + ((i - threshold)) / ratio

    return (i * under) + (k_red * inKnee) + (i * over_red)


def soft_knee_2(i,t,r,k):
    # A Simple soft_knee compression curve
    # Source: https://se.mathworks.com/help/audio/ref/compressor-class.html
    # Input: 1d np.array(), Threshold, Ratio, Knee width
    under = np.array([x for x in i if x < (t - k/2)])
    inKnee = np.array([x for x in i if (t - k/2) <= x and x <= (t + k/2)])
    over = np.array([x for x in i if (t + k/2) < x])

    k_f = (1/r - 1)
    intermediate = inKnee - t + k/2
    intermediate_pow = pow(intermediate,2)
    k_div_amnt = 2 * k
    k_mod = (k_f * intermediate_pow) / k_div_amnt
    k_red = inKnee + k_mod

    over_red = t + ((over - t)) / r

    return np.concatenate((under,k_red,over_red))


def hard_knee(i,t,r):
    """
    A Simple hard knee transfer function
    Input: np.array(), 1d,
    Threshold
    Ratio
    """
    under = np.array([x for x in i if x < t])
    over = np.array([x for x in i if x >= t])
    compressed = t + ((over - t) / R)
    return np.concatenate((under,compressed))


def shape(x):
    #An example shaping function
    return (4/9 * pow(x,6)) - (17/9 * pow(x,4)) + (22/9 * pow(x,2))
