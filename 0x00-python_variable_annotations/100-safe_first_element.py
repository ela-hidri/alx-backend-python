#!/usr/bin/env python3
"""
duck-typed annotations function  safe_first_elemen
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element
    """
    if lst:
        return lst[0]
    else:
        return None
