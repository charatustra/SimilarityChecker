from unittest import TestCase

from checker import Checker


class TestChecker(TestCase):
    def test_checker_length_max(self):
        checker = Checker()
        result = checker.check("ASD", "DSA")
        self.assertEqual(60, result)
