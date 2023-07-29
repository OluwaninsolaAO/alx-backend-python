#!/usr/bin/env python3
"""Unittest for Client Module"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestGithubOrgClient(unittest.TestCase):
    """Test Caseses for client.GithubOrgClient"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, name: str):
        """Tests client.GithubOrgClient works correctly with get_json"""
        with patch('client.get_json', return_value=None) as p_get_json:
            org = GithubOrgClient(name)
            org.org
            url = 'https://api.github.com/orgs/{name}'
            p_get_json.assert_called_once_with(url.format(name=name))


if __name__ == '__main__':
    unittest.main()
