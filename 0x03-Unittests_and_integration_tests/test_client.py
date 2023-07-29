#!/usr/bin/env python3
"""Unittest for Client Module"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD
from typing import Callable, Dict


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

    @patch('client.get_json', return_value=TEST_PAYLOAD[0][1])
    def test_public_repos(self, p_get_json: Callable):
        """Tests client.GithubOrgClient.public_repos"""

        resp = {'repos_url': 'https://api.github.com/orgs/Google/repos'}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock, return_value=resp)\
                as m_org:
            org = GithubOrgClient('Google')
            # self.assertEqual(org._public_repos_url, resp['repos_url'])
            self.assertEqual(org.public_repos(),
                             ['episodes.dart', 'cpp-netlib',
                              'dagger', 'ios-webkit-debug-proxy',
                              'google.github.io', 'kratu',
                              'build-debian-cloud', 'traceur-compiler',
                              'firmata.py'])
            m_org.assert_called_once()
            p_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, license_key: str,
                         expected: bool):
        """Tests GithubOrgClient.has_license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


if __name__ == '__main__':
    unittest.main()
