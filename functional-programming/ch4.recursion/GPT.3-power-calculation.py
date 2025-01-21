# Write a recursive function to calculate xyx^y (x raised to the power y).
# Example:
# power(2, 3)  # Output: 8 (2 * 2 * 2)

def power(x, y):
    if y == 0:
        return 1
    if x == 0:
        if y > 0:
            return 1
        if y < 0:
            raise ZeroDivisionError("Cannot power 0 to a negative number")
    if y > 0:
        return x * power(x, y - 1)
    if y < 0:
        return 1 / power(x, -y)
    
print(power(0, 0))
print(power(0, 1))
print(power(2, 3))
print(power(3, 3))
print(power(2, -3))
print(power(3, -3))