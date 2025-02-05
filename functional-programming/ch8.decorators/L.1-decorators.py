# The provided file_type_aggregator function is intended to decorate other functions. It assumes 
# that the function it decorates has exactly 2 positional arguments.
# 
# Create a process_doc function that's decorated by file_type_aggregator. It should return the following string:
# 
# f"Processing doc: '{doc}'. File Type: {file_type}"
# 
# Where doc and file_type are its positional arguments. (See line 11 for where it's being called)

def file_type_aggregator(func_to_decorate):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper

# don't touch above this line

@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: '{doc}'. File Type: {file_type}"

doc1 = "Welcome to the jungle"
file_type1 = "txt"
print(process_doc(doc1, file_type1))

doc2 = "We've got fun and games"
file_type2 = "txt"
print(process_doc(doc2, file_type2))

doc3 = "We've got *everything* you want honey"
file_type3 = "md"
print(process_doc(doc3, file_type3))