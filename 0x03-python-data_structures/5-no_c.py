#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all occurrences of 'c' and 'C' from a string.

    Args:
        my_string (str): The input string.

    Returns:
        str: The string with 'c' and 'C' removed.
    """
    new_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_string += elements
    return new_string
