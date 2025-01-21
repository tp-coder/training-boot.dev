# Complete the find_longest_word function without a loop. It accepts string inputs, document, 
# and optional longest_word, which is the current longest word and defaults to an empty string.
# - Check if the first word is longer than the current longest_word, then recur for the rest of the document.
# - Ensure there are no potential index errors.

def find_longest_word(document, longest_word=""):
    words = document.split()

    if not words:
        return longest_word
    
    current_word = words[0]
    if len(current_word) > len(longest_word):
        longest_word = current_word

    return find_longest_word(" ".join(words[1:]), longest_word) 

print(find_longest_word("this is a testo"))
print(find_longest_word("this is a test", "test"))