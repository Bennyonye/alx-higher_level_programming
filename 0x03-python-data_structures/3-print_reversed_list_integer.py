#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list, in reverse order.

    Args:
        my_list (list): The input list.

    Returns:
        None
    """
    if my_list:
        for elm in my_list[::-1]:
            print("{:d}".format(elm))
