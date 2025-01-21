# Complete the new_clipboard function. It accepts a dictionary as input and 
# returns two functions, copy_to_clipboard and paste_from_clipboard. It should 
# not modify the original input dictionary.
#
# - copy_to_clipboard: It takes a key and value string pair and adds them to the 
# clipboard dictionary.
# - paste_from_clipboard: It takes a key string and returns its value from the clipboard 
# dictionary. If the key is missing from the clipboard, return an empty string.

def new_clipboard(initial_clipboard):
    
    initial_dict = initial_clipboard.copy()

    def copy_to_clipboard(key, value):
        initial_dict[key] = value 
        return initial_dict
    
    def paste_from_clipboard(key):
        if key in initial_dict:
            return initial_dict[key]
        return ""

    return copy_to_clipboard, paste_from_clipboard