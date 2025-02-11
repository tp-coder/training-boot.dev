# Doc2Doc keeps track of how many words are in a collection of documents.
# 
# Complete the word_count_aggregator function. It should return a function that 
# calculates the number of words in its input (doc, a string). It should then add 
# that number to an enclosed count value and return the new count. In other words, 
# it keeps a running total of the count variable within a closure.

def word_count_aggregator():
    count = 0
    def word_count_inner(doc):
        nonlocal count
        count += len(doc.split())
        return count
    return word_count_inner

text = word_count_aggregator()
text("Welcome to the jungle")
text("We've got fun and games")
text("We've got everything you want honey")
print(text)

def word_count(doc):
    count = 0
    for word in doc.split():
        count += 1
    return count

print(word_count("How many words this text has?"))
