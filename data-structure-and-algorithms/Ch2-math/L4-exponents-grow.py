# Exponents Grow
# Exponents grow very large very quickly. Let’s take a look at an example of them doing that, in code.
#
# Assignment
# While the influencers who use our platform are really great at taking selfies, most aren’t super great at 
# math. We need to write a tool that predicts an influencer’s follower growth over time.
#
# Complete the get_follower_prediction function.
#
#  - “fitness” influencers: follower count quadruples each month
#  - “cosmetic” influencers: follower count triples each month
#  - All other influencers: follower count doubles each month
#
# For example, if a fitness influencer starts with 10 followers, then after 1 month they should have 40 
# followers. After 2 months, they would have 160 followers; etc.
#
# Use a geometric sequence formula that’s slightly modified for this problem: total = a1 * r^n

def get_follower_prediction(follower_count, influencer_type, num_months):
    # chose match over if-elif-else to allow for seamsless addition of new influencer types
    match influencer_type:
        case "fitness":
            return follower_count * (4 ** num_months)
        case "cosmetic":
            return follower_count * (3 ** num_months)
        case _:
            return follower_count * (2 ** num_months)