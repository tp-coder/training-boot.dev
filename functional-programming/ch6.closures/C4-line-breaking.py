# Complete the inner add_word_to_lines function. It takes a list of strings, lines, 
# and a string word, as inputs and returns lines with the word added.
#
# 1. If lines is empty, return just word in a list
# 2. Assign the last line in lines to current_line
# 3. If the length of current_line and word plus one (for a space) is more than line_length, 
# start a new line by appending word to lines
# 4. Else, add word to current_line with a space, and assign the new string to the last index in lines
# 5. Remember to return lines
# Note: Every line will have at least one word, even if that word is longer than the line_length.

from functools import reduce

def lineator(line_length):
    def lineate(document):
        words = document.split()

        def add_word_to_lines(lines, word):
            nonlocal line_length 
            if not lines:
                return [word]
            current_line = lines[-1]
            if len(current_line + " " + word) > line_length:
                lines.append(word)
            else:
                lines[-1] = f"{current_line} {word}"
            return lines

        return reduce(add_word_to_lines, words, [])

    return lineate

lineate = lineator(11)
lines = lineate("Boots loves salmon because he is a bear.")
# lines: ["Boots loves", "salmon", "because he", "is a bear."]
print(lines)