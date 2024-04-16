#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def parse_positive_integer(arg):
    """
    Parses a string argument and returns the corresponding positive integer.

    Args:
        arg (str): The string argument to be parsed.

    Returns:
        int or None: The positive integer value if the argument is a valid positive integer,
        None otherwise.
    """
    try:
        num = int(arg)
        return num if isinstance(num, int) and num > 0 else None
    except ValueError:
        return None
