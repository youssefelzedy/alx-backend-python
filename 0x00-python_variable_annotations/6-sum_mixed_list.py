#!/usr/bin/env python3

'''Sum a list of floats and integers and return their sum as a float'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Function that takes a list of floats and integers and returns their sum '''
    return sum(mxd_lst)
