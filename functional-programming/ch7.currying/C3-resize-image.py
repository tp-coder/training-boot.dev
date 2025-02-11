# 1. Complete the new_resizer function using currying. It takes integer inputs max_width 
# and max_height and returns an inner function.
#
# 2. The inner function should take optional integer inputs min_width and min_height — with 
# default values 0 — and return an innermost function.
#  - If min_width is more than max_width or min_height is more than max_height, raise an 
# exception "minimum size cannot exceed maximum size".
#
# 3. The innermost function should take two integer inputs width and height and return two integers.
#  - Use the built-in min and max functions to reduce or increase the width and height as needed, 
# then return the new width and new height.

def new_resizer(max_width, max_height):
    
    def min_size(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")
        
        def final_size(width, height):
            final_width = max(min_width, min(max_width, width))
            final_height = max(min_height, min(max_height, height))
            
            return (final_width, final_height)

        return final_size

    return min_size

# With currying syntax
print(new_resizer(800, 600)(200, 100)(1000, 500))  # Output: (800, 500)