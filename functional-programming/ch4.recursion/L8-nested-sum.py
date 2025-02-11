# Complete the sum_nested_list function. It takes a nested list of integers as input and should 
# return the total size of all files in the list. It's a recursive function.
# 
# Here's some pseudocode to help you get started:
# 
# Create an integer variable to keep track of the total size.
# 1. For each item in the list (use a loop here):
# 2. If the item is an integer, add it to the total size.
#   1. If the item is a list, use a recursive call to sum_nested_list to get the size of that list. Add that size to the total size.
#   2. Return the total size when you're done iterating.

def sum_nested_list(lst):
    total_size = 0

    if len(lst) == 0:
        return total_size

    for item in lst:
        if isinstance(item, list):
            total_size += sum_nested_list(item)
        else:
            total_size += item

    return total_size

root = [1, 2, [3, 4]]
print(sum_nested_list(root))
test = []
print(sum_nested_list(test))

