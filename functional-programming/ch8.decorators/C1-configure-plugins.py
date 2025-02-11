# Complete the configure_plugin_decorator function. It decorates a func that takes keyword 
# arguments **kwargs, but the wrapper function it returns takes positional arguments *args. 
# The arguments passed to the wrapper will be a series of tuples, each a key/value pair.
# 
# 1. Convert the args into a dictionary with the dict function.
# 2. Get the result of passing this dictionary into the func as keyword arguments unpacked with the ** operator.
# 3. Return the result.

def configure_plugin_decorator(func):
    def wrapper(*args):
        return func(**(dict(args)))
    return wrapper