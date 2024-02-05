#!/usr/bin/env python3
"""testing utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Tuple, Union, Dict
from unittest.mock import MagicMock
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    testing access_nested_map
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
        self.assertEqual(access_nested_map(nested_map, path), expected)
   
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
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    testing  get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        test correct result
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)
