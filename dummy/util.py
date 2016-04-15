# -*- coding: utf-8 -*-

from numba import njit

@njit(cache=True)
def barfoo():
    return 20


@njit(cache=True)
def bar():
    return barfoo()
