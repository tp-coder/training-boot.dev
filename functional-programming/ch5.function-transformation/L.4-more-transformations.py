# Complete the doc_format_checker_and_converter function.
#
# It takes a conversion_function and a list of valid_formats as parameters. It should return 
# a new function that takes two parameters of its own:
#   - filename: The name of the file to be converted
#   - content: The content (body text) of the file to be converted
# If the file extension of the filename is in the valid_formats list, then it should 
# return the result of calling the conversion_function on the content. Otherwise, it should 
# raise a ValueError with the message Invalid file format.

def doc_format_checker_and_converter(conversion_function, valid_formats):
    def file_format_checker(filename, content):
        if filename in valid_formats:
            return doc_format_checker_and_converter(conversion_function=content)
        raise ValueError("Invalid file format")
    return file_format_checker


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
