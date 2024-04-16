import unittest

from heiwa4126.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """
    A test case for the fizzbuzz function.
    """

    def test_fizzbuzz(self):
        """
        Test case for the fizzbuzz function.

        The test case verifies that the fizzbuzz function returns the correct output for the first 15 numbers.
        """
        result = list(fizzbuzz(15))
        self.assertEqual(
            result,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        )

    def test_fizzbuzz_custom_range(self):
        """
        Test case for the fizzbuzz function.

        The test case verifies that the fizzbuzz function returns the correct output for the first 20 numbers.
        """
        result = list(fizzbuzz(20))
        expected = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
            "16",
            "17",
            "Fizz",
            "19",
            "Buzz",
        ]
        self.assertEqual(result, expected)

    def test_fizzbuzz_empty_range(self):
        """
        Test case to verify the behavior of fizzbuzz function when given an empty range.
        """
        result = list(fizzbuzz(0))
        self.assertEqual(result, [])

    def test_fizzbuzz_negative_range(self):
        """
        Test case to verify the behavior of the fizzbuzz function when given a negative range.
        """
        result = list(fizzbuzz(-10))
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
