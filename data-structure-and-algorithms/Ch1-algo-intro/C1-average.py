# Average:
# We now need a way to show our LockedIn influencers the average follower count of the people they 
# follow. This will help them know if they’re following people who are more or less popular than them.
#
# Assignment:
# Complete the average_followers function. It should return the average of the given list of numbers.

def average_followers(nums):
    avg = 0
    if len(nums) == 0:
        return None
    for num in nums:
        avg+= num
    return avg / len(nums)