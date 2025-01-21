# Write a function to find the sum of the digits of a number using recursion.
# Example:
# sum_of_digits(1234)  # Output: 10 (1 + 2 + 3 + 4)

def sum_of_digits(n):
    if n == 0:
        return 0
    last_digit = n % 10 # extracts the last digit
    remaining_nums = n // 10 # removes the last digit
        
    return last_digit + sum_of_digits(remaining_nums)


print(sum_of_digits(1234))  # Output: 10
print(sum_of_digits(0))     # Output: 0
print(sum_of_digits(5))     # Output: 5
print(sum_of_digits(9999))  # Output: 36
