#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position without modifying the original list.

    Args:
        my_list (list): The input list.
        idx (int): The index at which the element should be replaced.
        element: The new element to be inserted.

    Returns:
        list: A new list with the specified replacement.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    else:
        new_list = list(my_list)
        new_list[idx] = element
        return new_list
