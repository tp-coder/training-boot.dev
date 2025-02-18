# Assignment
# We have a popular influencer using our LockedIn app, and she needs to be able to quickly search for posts from 
# a particular day. This function will be the backbone of her search screen.
#
# Complete the binary_search function. It should follow the algorithm as described above.

def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False