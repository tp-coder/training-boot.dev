# Edit Document
# Doc2Doc should be able to track changes in documents. Tracking changes is important for 
# undoing and redoing edits. Some editors save changes and some file formats do as well.
# 
# Assignment
# Complete the handle_edit function. It takes as input a document string, an edit_type EditType 
# enum, and an edit dictionary. It should use a match case statement to select the correct 
# operation depending on the EditType. Create a function to handle each operation as follows:
# 
# NEWLINE:
# Use the edit dictionary to modify and return a copy of the document. The edit dictionary will 
# only contain a line_number key and integer value (zero-indexed!). Add a newline \n at the end 
# of the line of the document corresponding to the line_number.
# 
# SUBSTITUTE:
# Use the edit dictionary to modify and return a copy of the document. The edit dictionary will 
# contain a insert_text key and string value, a line_number key and integer value, a start key 
# and integer value and an end key and integer value. Substitute the insert_text into the line of 
# the document corresponding to the line_number between the start and end indexes.
# 
# INSERT:
# Use the edit dictionary to modify and return a copy of the document. The edit dictionary will 
# contain a insert_text key and string value, a line_number key and integer value, and a start key 
# and integer value. Insert the insert_text into the line of the document corresponding to the 
# line_number at the start index.
# 
# DELETE:
# Use the edit dictionary to modify and return a copy of the document. The edit dictionary will 
# contain a line_number key and integer value, a start key and integer value, and an end key and 
# integer value. Remove the substring of the line of the document corresponding to the line_number 
# between the start and end indexes.
# 
# Exceptions:
# If the edit_type is none of the above, raise an Exception with the string "unknown edit type".

from enum import Enum

class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4

def handle_edit(document, edit_type, edit):
    match (edit_type):
        case (EditType.NEWLINE):
            return newline(document, edit)
        case (EditType.SUBSTITUTE):
            return insert_or_substitute(document, edit)
        case (EditType.INSERT):
            return insert_or_substitute(document, edit)
        case (EditType.DELETE):
            return delete(document, edit)
        case _:
            raise Exception("unknown edit type")     
    
def newline(document, edit):
    lines = document.split("\n")
    line_number = edit["line_number"]
    lines[line_number] += "\n"
    return "\n".join(lines)

def insert_or_substitute(document, edit):
    lines = document.split("\n")
    line_number = edit["line_number"]
    start = edit["start"]
    insert_text = edit["insert_text"]

    if "end" in edit:
        end = edit["end"]
        lines[line_number] = lines[line_number][:start] + insert_text + lines[line_number][end:]
    else:
        lines[line_number] = lines[line_number][:start] + insert_text + lines[line_number][start:]
    
    return "\n".join(lines)

def delete(document, edit):
    lines = document.split("\n")
    line_number = edit["line_number"]
    start = edit["start"]
    end = edit["end"]
    lines[line_number] = lines[line_number][:start] + lines[line_number][end:]
    return "\n".join(lines)
    
