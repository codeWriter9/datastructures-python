# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.strings.UniqueCharacter import UniqueCharacter


class TestStack(unittest.TestCase):

    def test_unique_character_not_null(self):
        self.assertIsNotNone(UniqueCharacter())

    def test_unique_character(self):
        self.assertEqual(0, UniqueCharacter.first_uniq_char("leetcode"))
        self.assertEqual(2, UniqueCharacter.first_uniq_char("loveleetcode"))
        self.assertEqual(-1, UniqueCharacter.first_uniq_char("aabb"))

