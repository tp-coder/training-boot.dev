# Complete the count_nested_levels function.
#
# 1. Loop over document_ids in the nested_documents dictionary
# 2. If the current document_id matches the target_document_id, return its level of nesting
# 3. If the target_document_id is not found, recursively call count_nested_levels on the current document_id and increment the level
#   - If it found the target_document_id's level, return it
# 4. If the target_document_id doesn't exist, the function should return -1

def count_nested_levels(nested_documents, target_document_id, level=1):
    
    if not nested_documents:
        return -1

    for document_id, subdocuments in nested_documents.items():
        if document_id == target_document_id:
            return level
        elif isinstance(subdocuments, dict):
            sublevel = count_nested_levels(subdocuments, target_document_id, level + 1)
            if sublevel != -1:
                return sublevel

    return -1

empty_documents = {}    
print(count_nested_levels(empty_documents, "docx"))
single_document = {1:{}}
print(count_nested_levels(single_document, 1))
nested_documents = {
    1: {
        3: {}
    },
    2: {}
}
print(count_nested_levels(nested_documents, 3))