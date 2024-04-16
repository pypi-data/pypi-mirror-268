#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from heiwa4126.fizzbuzz import fizzbuzz
from heiwa4126.fizzbuzz.parse import parse_positive_integer


def usage():
    print("Usage: heiwa4126_fizzbuzz <positive number>", file=sys.stderr)
    exit(1)


def main():
    """
    Entry point of the FizzBuzz program.

    Reads a positive integer from the command line argument and prints the FizzBuzz sequence up to that number.

    Usage:
        python cli.py <end>

    Args:
        end (int): The end number of the FizzBuzz sequence.

    Returns:
        None
    """
    if len(sys.argv) != 2:
        usage()

    end = parse_positive_integer(sys.argv[1])

    if end is None:
        usage()

    print("\n".join(fizzbuzz(end)))


if __name__ == "__main__":
    main()
