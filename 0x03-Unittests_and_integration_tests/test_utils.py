#!/usr/bin/env python3
"""testing utils.access_nested_map"""
import unittest
from parameterized import parameterized
import utils
from typing import Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """
    testing map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_map(self, value1: Dict,
                 val2: Tuple[str], expected: Union[Dict, int]) -> None:
        """
        testing access_nested_map
        """
        self.assertEqual(utils.access_nested_map(value1, val2), expected)


if __name__ == '__main__':
    unittest.main()
