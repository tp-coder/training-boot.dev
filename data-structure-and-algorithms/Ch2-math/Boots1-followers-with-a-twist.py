# Exercise 1: Followers with a Twist
# Context: The influencer world just got more complex! Some influencers experience follower losses in months when 
# their growth type doesn’t align well with trends.
#
# Task:
# Write a function get_trended_follower_prediction(follower_count, influencer_type, num_months, trending).
#
# Influencer growth rates:
#
#  - “fitness”: quadruples in trendy months, doubles otherwise.
#  - “cosmetic”: triples in trendy months, halves otherwise.
#  - All others: doubles in trendy months, loses 10% of followers otherwise.
#
# The parameter trending is a list of booleans, with each value corresponding to whether that month is trendy 
# (True) or not (False). For example, [True, False, True] would describe 3 months, where the 1st and 3rd are trendy.
#
# Return the final follower count after the given months.

def get_trended_follower_prediction(follower_count, influencer_type, trending):
    for trend in trending:
        match influencer_type:
            case "fitness":
                follower_count = follower_count * (4 if trend else 2)
            case "cosmetic":
                follower_count = follower_count * (3 if trend else 0.5)
            case _:
                follower_count = follower_count * (2 if trend else 0.9)
    return follower_count

# Test cases
print(get_trended_follower_prediction(10, "fitness", [True, False])) # 80
print(get_trended_follower_prediction(10, "fitness", [True, True])) # 160
print(get_trended_follower_prediction(10, "fitness", [False, False])) # 40
print(get_trended_follower_prediction(10, "cosmetic", [True, False])) # 15
print(get_trended_follower_prediction(10, "cosmetic", [True, True])) # 45
print(get_trended_follower_prediction(10, "cosmetic", [False, False])) # 5
print(get_trended_follower_prediction(10, "other", [True, False])) # 20
print(get_trended_follower_prediction(10, "other", [True, True])) # 40
print(get_trended_follower_prediction(10, "other", [False, False])) # 9
