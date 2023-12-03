#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position.

    Args:
        my_list (list): The input list.
        idx (int): The index at which the element should be replaced.
        element: The new element to be inserted.

    Returns:
        list: The modified list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the original list if the index is out of range
    else:
        my_list[idx] = element
        return my_list
