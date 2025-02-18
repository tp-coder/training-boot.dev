# Assignment
# LockedIn needs a new tool that allows big brands to see how many of an influencer's followers are loyal to their 
# brand. Complete the get_avg_brand_followers function. It takes two inputs:

# all_handles: a 2-dimensional list, or "list of lists" of strings representing user handles on a per-influencer 
# basis.
# brand_name: a string.
# get_avg_brand_followers returns the average number of handles that contain the brand_name across all the lists. 
# Each list represents the audience of a single influencer.
#
# Example Input/Output
# Input:
# all_handles = [
#     ["cosmofan1010", "cosmogirl", "billjane321"],
#     ["cosmokiller", "gr8", "cosmojane3"],
#     ["iloveboots", "paperthin"]
# ]
# brand_name = "cosmo"
# Expected output: 1.33 (handles per influencer, because 4 handles contained "cosmo" and there are 3 lists)

def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                count += 1
    return count / len(all_handles)

# test cases
all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]  
brand_name = "cosmo"
print(get_avg_brand_followers(all_handles, brand_name)) # expected 1.33
all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]
brand_name = "cosmogirl"
print(get_avg_brand_followers(all_handles, brand_name)) # expected 0.33