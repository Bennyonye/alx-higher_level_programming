#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
        my_list (list): The input list.

    Returns:
        A new list with True or False, indicating whether each integer in the original list is a multiple of 2.
    """
    new_list = []
    if my_list:
        for num in my_list:
            new_list.append(False if num % 2 else True)
        return new_list

