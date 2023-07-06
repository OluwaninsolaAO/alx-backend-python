#!/usr/bin/env python3
"""5. Complex types - list of floats"""


def sum_list(input_list: list[float]) -> float:
    """Return a sum of all numbers in input list"""
    result: float = 0
    for input in input_list:
        result = result + input
    return result
