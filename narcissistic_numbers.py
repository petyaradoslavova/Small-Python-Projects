def narcissistic(value):
    sum_of_digits = sum(int(digit) ** len(str(value)) for digit in str(value))
    if sum_of_digits == value:
        return True
    return False


print(narcissistic(153))
print(narcissistic(140))

# for num in [int(n) for n in str(value)]:
#     result += num ** len([int(n) for n in str(value)])