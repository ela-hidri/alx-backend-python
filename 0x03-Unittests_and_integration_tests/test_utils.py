#!/usr/bin/env python3
"""testing utils.access_nested_map"""
import unittest
from parameterized import parameterized
import utils
from typing import Tuple, Union, Dict


class TestAccessNestedMap(unittest.TestCase):
    """
    testing map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """
        testing access_nested_map
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
   
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str]) -> None:
        """
        check for KeyError
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
