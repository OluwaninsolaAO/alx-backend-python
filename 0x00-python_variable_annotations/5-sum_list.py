#!/usr/bin/env python3
"""5. Complex types - list of floats"""


def sum_list(input_list: list[float]) -> float:
    """Return a sum of all numbers in input list"""
    from functools import reduce
    return reduce(lambda x, y: x + y, input_list)
