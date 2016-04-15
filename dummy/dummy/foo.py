# -*- coding: utf-8 -*-

from numba import njit

from ..util import bar


@njit(cache=True)
def foo():
    return bar()
