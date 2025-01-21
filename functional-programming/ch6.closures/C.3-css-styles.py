# Complete the css_styles function. It accepts a nested dictionary as input, initial_styles, 
# and returns a function, add_style.
# 1. Copies initial_styles to avoid modifying the original dictionary.
# 2. Returns an add_style function that:
#  - Takes three string arguments: selector, property, and value. selector is a key in the initial_styles dictionary and its value should be a dictionary.
#  - Checks if the selector exists in the dictionary. If not, creates a new dictionary for the selector value.
#  - Then adds or updates the property with the given value for the selector.
#  - Returns the updated dictionary.

def css_styles(initial_styles):
    current_styles = initial_styles.copy()

    def add_style(selector, property, value):
        nonlocal current_styles
        if selector not in current_styles:
            current_styles[selector] = {property: value}
        current_styles[selector][property] = value
        return current_styles
        
    return add_style

initial_styles = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}

add_style = css_styles(initial_styles)
new_styles = add_style("p", "color", "grey")
print(new_styles)