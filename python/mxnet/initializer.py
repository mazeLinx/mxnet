# coding: utf-8
"""Initialization helper for mxnet"""
from __future__ import absolute_import

import numpy as np
from .base import string_types
from .ndarray import NDArray
from . import random

class Initializer(object):
    """Base class for Initializer."""

    def __call__(self, name, arr):
        """Override () function to do Initialization

        Parameters
        ----------
        name : str
            name of corrosponding ndarray

        arr : NDArray
            ndarray to be Initialized
        """
        if not isinstance(name, string_types):
            raise TypeError('name must be string')
        if not isinstance(arr, NDArray):
            raise TypeError('arr must be NDArray')
        if name.startswith('upsampling'):
            self._init_bilinear(name, arr)
        elif name.endswith('bias'):
            self._init_bias(name, arr)
        elif name.endswith('gamma'):
            self._init_gamma(name, arr)
        elif name.endswith('beta'):
            self._init_beta(name, arr)
        elif name.endswith('weight'):
            self._init_weight(name, arr)
        elif name.endswith("moving_mean"):
            self._init_zero(name, arr)
        elif name.endswith("moving_var"):
            self._init_zero(name, arr)
        elif name.endswith("moving_avg"):
            self._init_zero(name, arr)
        else:
            self._init_default(name, arr)
    # pylint: disable=no-self-use, missing-docstring, invalid-name
    def _init_bilinear(self, _, arr):
        weight = np.zeros(np.prod(arr.shape), dtype='float32')
        shape = arr.shape
        f = shape[3] / 2.
        c = (2 * f - 1 - f % 2) / (2. * f)
        for i in range(np.prod(shape)):
            x = i % shape[3]
            y = (i / shape[3]) % shape[2]
            weight[i] = (1 - abs(x / f - c)) * (1 - abs(y / f - c))
        arr[:] = weight.reshape(shape)

    def _init_zero(self, _, arr):
        arr[:] = 0.0

    def _init_bias(self, _, arr):
        arr[:] = 0.0

    def _init_gamma(self, _, arr):
        arr[:] = 1.0

    def _init_beta(self, _, arr):
        arr[:] = 0.0

    def _init_weight(self, name, arr):
        """Abstruct method to Initialize weight"""
        raise NotImplementedError("Must override it")

    def _init_default(self, name, _):
        raise ValueError('Unknown initialization pattern for %s' % name)
    # pylint: enable=no-self-use, missing-docstring, invalid-name

class Uniform(Initializer):
    """Initialize the weight with uniform [-scale, scale]

    Parameters
    ----------
    scale : float, optional
        The scale of uniform distribution
    """
    def __init__(self, scale=0.07):
        self.scale = scale

    def _init_weight(self, _, arr):
        random.uniform(-self.scale, self.scale, out=arr)


class Normal(Initializer):
    """Initialize the weight with normal(0, sigma)

    Parameters
    ----------
    sigma : float, optional
        Standard deviation for gaussian distribution.
    """
    def __init__(self, sigma=0.01):
        self.sigma = sigma

    def _init_weight(self, _, arr):
        random.normal(0, self.sigma, out=arr)


class Xavier(Initializer):
    """Initialize the weight with Xavier or similar initialization scheme.

    Parameters
    ----------
    rnd_type: str, optional
        Use ```gaussian``` or ```uniform``` to init

    factor_type: str, optional
        Use ```avg```, ```in```, or ```out``` to init

    magnitude: float, optional
        scale of random number range
    """
    def __init__(self, rnd_type="uniform", factor_type="avg", magnitude=3):
        self.rnd_type = rnd_type
        self.factor_type = factor_type
        self.magnitude = magnitude


    def _init_weight(self, _, arr):
        shape = arr.shape
        fan_in, fan_out = np.prod(shape[1:]), shape[0]
        factor = 1
        if self.factor_type == "avg":
            factor = (fan_in + fan_out) / 2
        elif self.factor_type == "in":
            factor = fan_in
        elif self.factor_type == "out":
            factor = fan_out
        else:
            raise ValueError("Incorrect factor type")
        scale = np.sqrt(self.magnitude / factor)
        if self.rnd_type == "uniform":
            random.uniform(-scale, scale, out=arr)
        elif self.rnd_type == "gaussian":
            random.normal(0, scale, out=arr)
        else:
            raise ValueError("Unknown random type")
