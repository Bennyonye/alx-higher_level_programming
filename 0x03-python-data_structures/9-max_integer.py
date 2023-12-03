#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds the maximum integer in a list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        int or None: The maximum integer or None if the list is empty.
    """
    new_list = []
    if my_list:
        my_list.sort(reverse=True)
        return (my_list[0])
    return (None)
