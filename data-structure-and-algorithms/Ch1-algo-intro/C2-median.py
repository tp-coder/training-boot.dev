# Median:
# A median is often more useful than an average when the data set contains outliers. For example, if you 
# want to know the typical salary of a software engineer, the median can be a better measure than the average, 
# because the average can be skewed by a few people who make a lot of money.

# At LockedIn, we want to show our influencers the median follower count of the people they follow.

# Assignment
# Complete the median_followers() function to find the median follower count of the given list of numbers.

# Order matters - You’ll probably want to use the sorted() function to help you out. Be sure to appropriately 
# handle lists of even length.

def median_followers(nums):
    nums.sort()
    n = len(nums)
    if n == 0:
        return None
    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    return nums[n//2]