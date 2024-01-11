#!/usr/bin/env python3
"""
type-annotated function  to_str
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_list function
    """
    return sum(mxd_lst)
