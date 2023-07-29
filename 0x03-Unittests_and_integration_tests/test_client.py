#!/usr/bin/env python3
"""Unittest for Client Module"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock


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

    def test_public_repos_url(self):
        """Tests client.GithubOrgClient._public_repos_url"""
        resp = {'repos_url': 'https://api.github.com/orgs/Google/repos'}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock, return_value=resp):
            org = GithubOrgClient('Google')
            self.assertEqual(org._public_repos_url, resp['repos_url'])


if __name__ == '__main__':
    unittest.main()
