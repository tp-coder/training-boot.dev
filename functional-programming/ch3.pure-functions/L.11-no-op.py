# Complete the remove_emphasis, remove_emphasis_from_line, and remove_emphasis_from_word functions.
# They are currently no-ops.
# remove_emphasis is the parent function. 
# It takes a full document and removes any single or double * characters that are at the start or end of a word.

def remove_emphasis_from_word(word):
    return word.strip("*")

def remove_emphasis_from_line(line):
    words = line.split()
    new_words = map(remove_emphasis_from_word, words)
    return " ".join(new_words)
 
def remove_emphasis(doc_content):
    lines = doc_content.split("\n")
    new_lines = map(remove_emphasis_from_line, lines)
    return "\n".join(new_lines)
