# Logarithmic Scale
# In some cases, data can span several orders of magnitude, making it difficult to visualize on a linear scale. 
# A logarithmic scale can help by compressing the data so that it's easier to understand.
#
# For example, at LockedIn we have influencers with follower counts ranging from 1 to 1,000,000,000. If we want 
# to plot the follower count of each influencer on a graph, it would be difficult to see the differences between 
# the smaller follower counts. We can use a logarithmic scale to compress the data so that it's easier to visualize.
#
# Assignment
# Write a function log_scale(data, base) that takes a list of positive numbers data, and a logarithmic base, and 
# returns a new list with the logarithm of each number in the original list, using the given base.
#
# You may want to use the math.log() function.

import math

def log_scale(data, base):
    result = []
    for num in data:
        result.append(math.log(num, base))
    return result

#test cases
print(log_scale([1, 10, 100, 1000], 10)) # expected [0.0, 1.0, 2.0, 3.0]
print(log_scale([1, 10, 100, 1000], 2)) # expected [0.0, 3.321928094887362, 6.643856189774725, 9.965784284662087]
print(log_scale([1, 2, 4, 8], 2)) # expected [0.0, 1.0, 2.0, 3.0]