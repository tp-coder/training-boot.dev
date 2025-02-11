# Within Doc2Doc we need to map certain properties from one document to properties of another document. 
# Complete the recursive zipmap function.
#
# It takes two lists as input and returns a dictionary where the first list provides the keys and the second list provides the values.

def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    return {keys[0]: values[0]} | zipmap(keys[1:], values[1:])
