"""
Unit tests for text_adapter.py
Author: Camilla Montonen
"""

import unittest
import text_adapter

class TestTextAdapterFunctions(unittest.TestCase):

    def setUp(self):
        self.text_data=["Hello send your password", "hello please click link", "click link"]
        "your password here", "send password", "hello reset your password", "password email", "warm hello"]
    def test_dictionary_builder(self):
        self.dictionary=text_adapter.dictionary_builder(self.text_data)
        self.assertTrue("hello" in self.dictionary.keys())
        self.assertFalse("world" in self.dictionary.keys())


if __name__ == '__main__':
    unittest.main()
