#!/usr/bin/env python3

"""TestGithubOrgClient"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    '''TestGithubOrgClient'''

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        '''test_org'''
        mock_get_json.return_value = {"login": org_name}

        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(result, mock_get_json.return_value)
