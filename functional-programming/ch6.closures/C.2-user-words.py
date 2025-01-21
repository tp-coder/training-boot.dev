# Complete the 'user_words' function. It accepts a tuple of initial_words 
# as input and returns a function, add_word. Since tuples are immutable, 
# you don't need to worry about modifying the initial_words. add_word should 
# add a new word string to the words and return all words as a tuple.

def user_words(initial_words):
    new_words = initial_words
    def add_word(word):
        nonlocal new_words
        new_words += (word,)
        return new_words
    return add_word

initial_words = ('cap',)
add_word = user_words(initial_words)

# Add multiple words
result = add_word(['bussin', 'salty'])
print(result)  # Output: ('cap', 'bussin', 'salty')
