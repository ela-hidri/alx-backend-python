#!/usr/bin/env python3
"""
duck-typed annotations function  safe_first_elemen
"""

from typing import Any, Mapping, Sequence, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any, 
                     default: Union[TypeVar('T'), None] = None
                     )-> Union[Any, TypeVar('T')]:
    """
    safely_get_value
    """
    if key in dct:
        return dct[key]
    else:
        return default
