# For the LockedIn influencer dashboard, we need to calculate the total reach of a group of influencers to 
# estimate how many views a post will get if they all share it.
#
# Complete the sum function. It’s a slightly modified version of the algorithm above. Instead of just two 
# numbers, a and b, it accepts a list of numbers and returns the sum of all of them.
#
# Note: The sum of an empty list should be 0.

def sum(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum