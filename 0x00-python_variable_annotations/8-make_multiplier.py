#!/usr/bin/env python3

''' Make a multiplier function that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.'''


def make_multiplier(multiplier: float) -> callable:
    ''' Function that takes a float multiplier and returns a function that multiplies a float by multiplier '''
    def multiply(n: float) -> float:
        ''' Function that takes a float and returns its product with multiplier '''
        return n * multiplier
    return multiply
