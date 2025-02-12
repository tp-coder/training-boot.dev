# Exercise 2: Plants and Growth
# Context: You are a horticultural wizard growing magical plants in pots. Each type of plant grows at a different 
# rate, and the number of pots influences how much you have to split your magic per plant.
#
# Task:
# Write a function calculate_plant_growth(initial_growth, pot_count, plant_type, num_days).
#
# Growth rates:
#  - “carnivorous”: daily growth rate is 1.8^num_days / pot_count
#  - “flowering”: daily growth rate is 1.5^num_days / pot_count
#  - “herbs”: daily growth rate is 1.2^num_days / pot_count
#  - Others: daily growth rate is 1.1^num_days / pot_count
#
# Return the total new growth after the given days (initial_growth + accumulated growth). For instance, if you 
# start with 10 growth and calculate +5 growth over time, return 15.

def calculate_plant_growth(initial_growth, pot_count, plant_type, num_days):
    match plant_type:
        case "carnivorous":
            accumulated_growth = 1.8 ** num_days / pot_count
        case "flowering":
            accumulated_growth = 1.5 ** num_days / pot_count
        case "herbs":
            accumulated_growth = 1.2 ** num_days / pot_count
        case _:
            accumulated_growth = 1.1 ** num_days / pot_count
    return initial_growth + accumulated_growth

# Test cases
# Test 1: One carnivorous plant, one pot, one day
print(calculate_plant_growth(10, 1, "carnivorous", 1))  # Should be 11.8
# Test 2: One carnivorous plant, two pots, one day
print(calculate_plant_growth(10, 2, "carnivorous", 1))  # Should be 10.9 (less growth per plant due to split magic)
# Test 3: One flowering plant, one pot, two days
print(calculate_plant_growth(10, 1, "flowering", 2))  # Should be 12.25 (10 + 1.5^2)
# More days (exponential growth becomes more apparent)
print("5 days with carnivorous plant:")
print(calculate_plant_growth(10, 1, "carnivorous", 5))  # 1.8^5 is much larger!
# Many pots (testing division effects)
print("\nMany pots splitting the magic:")
print(calculate_plant_growth(10, 10, "flowering", 3))  # Growth split among 10 pots
# Unknown plant type (testing default case)
print("\nMystery plant:")
print(calculate_plant_growth(10, 1, "mushroom", 2))  # Should use 1.1 as base
# Larger initial growth
print("\nLarge initial growth:")
print(calculate_plant_growth(100, 1, "herbs", 4))  # Starting with 100 instead of 10