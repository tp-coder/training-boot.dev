# Write a recursive function to calculate the 𝑛 n-th Fibonacci number.
# Example:
# fibonacci(6)  # Output: 8 (0, 1, 1, 2, 3, 5, 8)

def fibonacci(n):
    if n == 0:
        return (0,)
    if n == 1:
        return (0, 1)
    
    previous_sequence = fibonacci(n - 1)
    next_number = previous_sequence[-1] + previous_sequence[-2]

    return previous_sequence + (next_number,)

print(fibonacci(7))

def fibonacci_in_memo(n, memo={}):
    if n == 0:
        return (0,)
    if n == 1:
        return (0, 1) 
    # using memoization dictionary
    if n in memo:
        return memo[n]
    
    previous_sequence = fibonacci_in_memo(n - 1, memo)
    next_number = previous_sequence[-1] + previous_sequence[-2]
    # storing the result in memo dict
    memo[n] = previous_sequence + (next_number, )

    return memo[n]

print(fibonacci_in_memo(7))