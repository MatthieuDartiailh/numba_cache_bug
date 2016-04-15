# -*- coding: utf-8 -*-

from numba import njit


@njit(cache=True)
def bar():
    return 0
