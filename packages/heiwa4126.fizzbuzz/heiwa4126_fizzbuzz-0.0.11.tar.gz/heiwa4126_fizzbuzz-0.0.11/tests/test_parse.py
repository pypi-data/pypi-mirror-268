import unittest

from heiwa4126.fizzbuzz.parse import parse_positive_integer


class TestParse(unittest.TestCase):
    def test_parse_positive_integer_valid(self):
        """
        Test case to verify that parse_positive_integer returns the correct output for valid positive integers.
        """
        result = parse_positive_integer("10")
        self.assertEqual(result, 10)

    def test_parse_positive_integer_invalid(self):
        """
        Test case to verify that parse_positive_integer returns None for invalid inputs.
        """
        result = parse_positive_integer("abc")
        print(result)
        self.assertIsNone(result)

    def test_parse_positive_integer_zero(self):
        """
        Test case to verify that parse_positive_integer returns None for zero.
        """
        result = parse_positive_integer("0")
        self.assertIsNone(result)

    def test_parse_positive_integer_negative(self):
        """
        Test case to verify that parse_positive_integer returns None for negative numbers.
        """
        result = parse_positive_integer("-10")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
