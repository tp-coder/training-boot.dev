# Assignment
# LockedIn needs search capabilities! For now, we'll build something slow (and frankly awful) so we can see an n^2 
# algorithm in practice.

# Complete the does_name_exist function. It should loop over all of the first/last name combinations in the 
# first_names and last_names lists. If it finds a combination that matches the full_name it should return True. 
# If the full name isn't found, it should return False instead.

# Observe
# When you run your completed code, notice how each successive call to does_name_exist takes quite a bit longer. 
# Assuming the length of first_names and last_names is the same, each new name doesn't add n steps to the algorithm; 
# the total number of steps grows quadratically with the size of the input, making the total work O(n^2).
#
# If does_name_exist(10 names, 10 names) takes just 1 second to complete, then we can estimate:
#  - does_name_exist(100 names, 100 names) = 100 seconds
#  - does_name_exist(1000 names, 1000 names) = 10,000 seconds
#  - does_name_exist(10000 names, 10000 names) = 1,000,000 seconds

def does_name_exist(first_names, last_names, full_name):
    for name in first_names:
        for surname in last_names:
            if f'{name} {surname}' == full_name:
                return True
    return False

# test cases
print(does_name_exist(["John", "Jane", "Mike"], ["Doe", "Smith", "Jones"], "Jane Smith")) # expected True
print(does_name_exist(["John", "Jane", "Andrew"], ["Doe", "Smith", "Jones"], "Mike Smith")) # expected False
print(does_name_exist(["John", "Jane", "Mike"], ["Doe", "Smith", "Jones"], "Mike Jones")) # expected True
print(does_name_exist(["John", "Jane", "Mike"], ["Dude", "Smith", "Jones"], "John Doe")) # expected False
print(does_name_exist(["John", "Jane", "Mike"], ["Doe", "Smith", "Jones"], "John Smith")) # expected True