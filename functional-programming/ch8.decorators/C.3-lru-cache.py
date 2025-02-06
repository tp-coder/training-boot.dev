# The creator of Doc2Doc is a huge fan of palindromes for some nerdy reason. Add a feature 
# to check if a word is a palindrome.
# 
# Import the lru_cache function from the functools module. Use it to decorate the incomplete 
# is_palindrome function.
# 
# Complete the is_palindrome function. It takes as input a word string and returns True if the 
# word is a palindrome (such as “racecar”), or False otherwise. Try to use recursion. Check the 
# outer characters first, then move inwards until you reach the base case or find the word is not 
# a palindrome.

from functools import lru_cache

@lru_cache()
def is_palindrome(word):
    if len(word) <= 1:
        return True
    
    if word[0] != word[-1]:
        return False
    
    new_word = word[1:-1]
    return is_palindrome(new_word)