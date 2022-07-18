# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/16/2022
# Description: Takes a list of numbers and returns the maximum value via a recursive function.

def list_max(num_list):
    """Returns the maximum value from a list of numbers."""

    if len(num_list) == 1:
        return num_list[0]

    if num_list[0] <= num_list[1]:
        return list_max(num_list[1:])
    else:
        return list_max(num_list[0:1] + num_list[2:])
