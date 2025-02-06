# Complete the replacer function.

# It takes as input two strings, old and new, and returns a function, replace.
#
# replace takes an input function, decorated_func, and returns a wrapper function.
# wrapper takes as input a string text. It uses .replace() string method to replace 
# instances of old with new in the text. Then it returns the result of passing the modified 
# text to the decorated_func.
#
# Use a series of the replacer function to decorate tag_pre. Pass the following pairs of 
# strings to these decorators to encode the escape sequences:
# - Replace "&" with "&amp;"
# - Replace "<" with "&lt;"
# - Replace ">" with "&gt;"
# - Replace '"' with "&quot;"
# - Replace "'" with "&#x27;"

def replacer(old, new):
    def replace(decorated_func):
        def wrapper(text):
            return decorated_func(text.replace(old, new))
        return wrapper
    return replace

@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")

def tag_pre(text):
    return f"<pre>{text}</pre>"
