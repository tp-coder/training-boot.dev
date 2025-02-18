# Assignment
# At LockedIn, we now need to display to our users the people who follow them with the highest engagement count. 
# This will help them know which of their followers they should follow back.
#
# Complete the find_max function. It should take a list of integers and return the largest value in the list.
#
# The "runtime complexity" (aka Big O) of this function should be O(n).

def find_max(nums):
    max_so_far = float('-inf')
    if len(nums) == 0:
        return None
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far

# test cases
print(find_max([1, 2, 3, 4])) # expected 4
print(find_max([1, 2, 3, 4, 4])) # expected 4
print(find_max([1, 2, 3, 4, 5])) # expected 5
print(find_max([5, 4, 3, 2, 1])) # expected 5
print(find_max([1])) # expected 1
print(find_max([])) # expected None
print(find_max([-1, -2, -3, -4])) # expected -1
print(find_max([-1, -2, -3, -4, -4])) # expected -1