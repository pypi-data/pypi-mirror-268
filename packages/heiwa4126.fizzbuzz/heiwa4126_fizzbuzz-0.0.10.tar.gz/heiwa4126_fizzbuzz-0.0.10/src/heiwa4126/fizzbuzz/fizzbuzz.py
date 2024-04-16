#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Generator


def fizzbuzz_at(n: int) -> str:
    """
    Return the FizzBuzz value at a given number.

    Args:
        n (int): The number at which the FizzBuzz value should be returned.

    Returns:
        str: The FizzBuzz value at the given number.

    Examples:
        >>> fizzbuzz_at(1)
        '1'
        >>> fizzbuzz_at(3)
        'Fizz'
        >>> fizzbuzz_at(5)
        'Buzz'
        >>> fizzbuzz_at(15)
        'FizzBuzz'
    """
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """
    Generate the FizzBuzz sequence up to a given number.

    Args:
        n (int): The number up to which the FizzBuzz sequence should be generated.

    Yields:
        str: The next element in the FizzBuzz sequence.

    Examples:
        >>> list(fizzbuzz(15))
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    """
    for i in range(1, n + 1):
        yield fizzbuzz_at(i)


if __name__ == "__main__":
    for result in fizzbuzz(15):
        print(result)
