# Doc2Doc needs a good logging system so that users and developers alike can see what's 
# going on under the hood. Complete the get_logger function.
#
# It takes a formatter function as a parameter and returns a new function. Steps:
# 1. Define a new function, logger, inside get_logger (see self_math above as an example). 
# It accepts two strings. You can just name them first and second if you like.
#
# 2. The logger function should not return anything. It should simply print the result 
# of calling the given formatter function with the first and second strings as arguments.
#
# 3. Return the new logger function for the test suite to use.

def get_logger(formatter):
    def logger(string1, string2):
        print(formatter(string1, string2))
    return logger


# Don't edit below this line


def test(first, errors, formatter):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first, second):
    return f"{first}: {second}"


def dash_delimit(first, second):
    return f"{first} - {second}"


def main():
    db_errors = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)


main()
