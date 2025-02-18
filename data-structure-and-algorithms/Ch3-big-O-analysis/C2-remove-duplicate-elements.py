# Remove Duplicate Elements
# We're interested in showing the unique follower counts of all of an influencer's followers.
#
# Assignment
# Complete the remove_duplicates function. It takes a list of integers nums and returns a new list of integers. 
# The returned list of integers should consist of all the unique follower counts in nums without any duplicates.
#
# We want to preserve the order of the list so be careful when using a set!

def remove_duplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    return result