#!/usr/bin/env python3
"""
type-annotated function  make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    to_kv function
    """
    def mul(x: float) -> float:
        return x * multiplier
    return mul
