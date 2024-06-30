#!/usr/bin/env python3

"""TEST Generic utilities for github org client.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''Test access_nested_map function
    '''
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a", "b"], 2),
        ({"a": {"b": {"c": 3}}}, ["a", "b", "c"], 3),
    ])
    def test_access_nested_map(self, mested_map, path, expected):
        self.assertEqual(access_nested_map(mested_map, path), expected)
