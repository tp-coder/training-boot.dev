# At Doc2Doc, we need better internal debugging tools. Complete the args_logger function. It 
# takes a variable number of positional and keyword arguments and prints them to the console.
# 
# Print each positional argument sequentially using numbers and periods as the prefixes, starting 
# with 1.. For example:
# args_logger("what's", "up", "doc")
#
# prints to the console:
# 
# 1. what's
# 2. up
# 3. doc
#
# Print each keyword argument alphabetically by key using asterisks (*) as the prefix with a colon (:) 
# in between. For example:
# args_logger("hi", "there", age=17, date="July 4 1776")
#
# prints to the console:

# 1. hi
# 2. there
# * age: 17
# * date: July 4 1776
# 
# Use the sorted() function to get the order right.

def args_logger(*args, **kwargs):
    for index, value in enumerate(args, start=1):
        print(f"{index}. {value}")
    for key in sorted(kwargs):
        print(f"* {key}: {kwargs[key]}")

args_logger("Good", "riddance", date_str="01/01/2023")