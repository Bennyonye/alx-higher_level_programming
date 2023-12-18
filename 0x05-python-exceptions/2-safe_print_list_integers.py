#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers in a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        The real number of integers printed.
    """
    count = 0

    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end=" ")
                count += 1
        except IndexError:
            break

    print("")
    return (count)
