# Fix the bug by making add_format and remove_format pure functions that don't mutate their inputs.

def add_format(default_formats, new_format):
    new_formats = default_formats.copy()
    new_formats[new_format] = True
    return new_formats


def remove_format(default_formats, old_format):
    old_formats = default_formats.copy()
    old_formats[old_format] = False
    return old_formats
