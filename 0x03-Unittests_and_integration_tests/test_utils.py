#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Mapping,
    Any,
    Sequence
)


class TestAccessNestedMap(unittest.TestCase):
    """Test Cases for Access Nested Map Function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence,
                               expected: Any):
        """Tests access_nested_map return expected Values"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """Tests access_nested_map raisees Exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        # self.assertEqual(str(context.exception), "")


if __name__ == '__main__':
    unittest.main()
