#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
        my_list (list): The input list.

    Returns:
        A new list with True or False, indicating whether each integer in the original list is a multiple of 2.
    """
    if my_list is None:
        return None
    listdivs = []
    for i in my_list:
        if (i % 2) == 0:
            listdivs.append(True)
        else:
            listdivs.append(False)
    return listdivs
