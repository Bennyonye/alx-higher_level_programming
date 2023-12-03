#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieves an element from a list.

    Args:
        my_list (list): The input list.
        idx (int): The index to retrieve the element.

    Returns:
        The element at the specified index, or None if the index is out of range.
    """
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]
