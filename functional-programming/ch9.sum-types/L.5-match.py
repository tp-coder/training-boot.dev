# Complete the convert_format function. Using the enum DocFormat, it should 
# support 3 types of conversions:
# 
# From MD to HTML:
# - Assume the content is a single h1 tag in markdown syntax - it’s a single string 
# representing a line. Replace the leading # with an <h1> and add a </h1> to the end.
# # This is a heading -> <h1>This is a heading</h1>
# 
# From TXT to PDF:
# - Simply add a [PDF] tag to the beginning and end of the content. Notice the 
# spaces between [PDF] tags and the content:
# This is some text -> [PDF] This is some text [PDF]
# 
# From HTML to MD:
# - Replace any <h1> tags with # and remove any </h1> tags.
# <h1>This is a heading</h1> -> # This is a heading
# 
# Any other conversion:
# -If the input format is invalid, raise an Exception with the string invalid type.

from enum import Enum

class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4

# don't touch above this line

def convert_format(content, from_format, to_format):
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            return content.replace("# ","<h1>", 1) + "</h1>"
        case (DocFormat.TXT, DocFormat.PDF):
            return f"[PDF] {content} [PDF]"
        case (DocFormat.HTML, DocFormat.MD):
            return content.replace("<h1>", "# ")[:-5]
        # for invalid cases
        case _:
            raise Exception("invalid type")
