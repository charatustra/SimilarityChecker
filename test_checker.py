from unittest import TestCase

from checker import Checker


class TestChecker(TestCase):
    def setUp(self):
        self.checker = Checker()

    def test_checker_length_max(self):
        self.assertEqual(60, self.checker.check("ASD", "DSA"))

    def test_checker_length_zero(self):
        self.assertEqual(0, self.checker.check("A", "BB"))
