# In Doc2Doc, depending on the type of text file we're working with, we sometimes need 
# to transform the font size of the text when it comes time to render it on the screen.
#
# Fix the converted_font_size function. We are using a 3rd party code library that expects 
# our function to be a curried series of functions that each take a single argument.
# - converted_font_size should just take a single argument, font_size and return a function 
# that takes a single argument, doc_type. That function should return the font_size multiplied 
# by the appropriate value for the given doc_type.

def converted_font_size(font_size):
    def check_doc_type(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("Invalid doc type")
    return check_doc_type

case1 = converted_font_size(14)("txt")
print(f"Expecting 14, got {case1}")
case2 = converted_font_size(10)("md")
print(f"Expecting 20, got {case2}")
case3 = converted_font_size(12)("docx")
print(f"Expecting 36, got {case3}")
case4 = converted_font_size(11)("zip")
print(f"Expecting Invalid doc type, got {case4}")