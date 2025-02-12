# Python Syntax
# There isn’t a language-level operator to calculate a logarithm, but we can import the math library and use the 
# math.log() function.
# import math
# print(f"Logarithm base 2 of 16 is: {math.log(16, 2)}")
# Logarithm base 2 of 16 is: 4.0
# 
# Assignment
# Let’s create an “influencer score”. It will be a small number (like less than 100) that will give influencers a 
# metric for comparing their social media success against their peers.
#
# Complete the get_influencer_score function. An influencer score is their engagement percentage multiplied by log 
# base 2 of their follower count.

import math

def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)