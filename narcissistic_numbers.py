def narcissistic(value):
    """Find if a number is narcissistic number - sum of its digits each raised to the power of the number of digits"""
    sum_of_digits = sum(int(digit) ** len(str(value)) for digit in str(value))
    if sum_of_digits == value:
        return True
    return False


print(narcissistic(153))
print(narcissistic(140))

