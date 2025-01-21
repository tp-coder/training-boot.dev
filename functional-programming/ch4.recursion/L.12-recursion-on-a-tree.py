# You're responsible for a module in Doc2Doc that can scan a file system 
# (represented in our code as nested dictionaries) and create a list of the filenames.
#
# Complete the recursive list_files function. It accepts two arguments:
# 1. parent_directory: A dictionary of dictionaries representing the current directory. 
# A child directory's value is a dictionary and a file's value is None.
# 2. current_filepath: A string representing the current path (e.g. /dir1/dir2/filename.txt)
# It should return a list of all filepaths in the parent_directory.
#
# Steps
# - Create an empty list to store the file paths.
# - Use a for-loop to iterate through the keys of the parent_directory dictionary:
#   - Use the key to create a new file path by concatenating a slash / and the key to the end of the current_filepath.
#   - If the value is None, the key is a filename. .append() the new file path to the list of file paths.
#   - Otherwise, the value is a child directory dictionary. Recursively call list_files with the child directory dictionary and the new file path.
#   - Use .extend() to add the results of the recursive call to the list of file paths.
# - Return the list of file paths.

def list_files(parent_directory, current_filepath=""):
    file_paths = []

    if not parent_directory:
        return file_paths
    
    for key, value in parent_directory.items():
        if value is None:
            file_paths.append(f"{current_filepath}/{key}")
        elif isinstance(value, dict):
            subdirectory = list_files(value, f"{current_filepath}/{key}")
            file_paths.extend(subdirectory)

    return file_paths

empty_directory = {}

single_file = {"test.txt":None}

single_directory = {
    "Documents": {
        "file.txt": None
    }
}

nested_directory = {
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {
                "receipt1.txt": None,
                "receipt2.txt": None
            },
            "February": {
                "receipt3.txt": None
            }
        }
    },
}

print(list_files(single_file))
print(list_files(single_directory))
print(list_files(nested_directory))