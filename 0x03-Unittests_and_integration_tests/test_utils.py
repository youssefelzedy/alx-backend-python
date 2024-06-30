#!/usr/bin/env python3

"""TEST Generic utilities for github org client.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertTrue(isinstance(context.exception, KeyError))

class TestGetJson(unittest.TestCase):
    '''Test get_json function
    '''
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, payload):
        with patch('requests.get') as mock_get:
            mock_respose = Mock()
            mock_respose.json.return_value = payload
            mock_get.return_value = mock_respose
        
            response = get_json(url)
        
            mock_get.assert_called_once_with(url)
            self.assertEqual(response, payload)