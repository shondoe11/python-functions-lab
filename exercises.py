# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.

def calculate_area_triangle(base, height):
    return base * height / 2

print('Exercise 1:', calculate_area_triangle(10, 5))
print(calculate_area_triangle(7, 3))


# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.

def simple_interest(principal, interest_rate, time):
    answer = (principal * interest_rate * time) / 100
    return int(answer) if answer.is_integer() else answer

print('Exercise 2:', simple_interest(1000, 5, 2))
print(simple_interest(1500, 3.5, 5))


# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.

def apply_discount(prod_price, disc_percentage):
    if prod_price < 0 or disc_percentage < 0 or disc_percentage > 100:
        return 'invalid discount or price'
    else:
        final_price = prod_price * (1 - disc_percentage / 100)
        return int(final_price) if final_price.is_integer() else final_price

print('Exercise 3:', apply_discount(100, 25))
print(apply_discount(80, 10))
print(apply_discount(1100, -2))
print(apply_discount(89.9, 20))


# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.

def convert_temperature(num, unit):
    unit = unit.lower()
    if unit not in ('c','f'):
        return 'invalid unit'
    elif unit == 'c': return (num * 9/5) + 32
    else: return (num - 32) * 5 / 9

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))
print(convert_temperature(32, 'B'))


# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.

def sum_to(n):
    if n < 1 or type(n) != int: return 'must be positive integer more than 0'
    return sum(range(1, n + 1))

print('Exercise 5:', sum_to(6))
print(sum_to(10))
print(sum_to(0.5))


# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.

def largest(int1, int2, int3):
    return max(int1, int2, int3)

print('Exercise 6:', largest(1, 2, 3))
print(largest(10, 4, 2))


# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.

def calculate_tip(bill, tip):
    if isinstance(bill, int) and isinstance(tip, int):
        tip_amt = bill * tip / 100
        if tip_amt.is_integer(): return int(tip_amt)
        else: return tip_amt
    else: return 'both bill and tip must be whole NUMBERs'

print('Exercise 7:', calculate_tip(50, 20))
print(calculate_tip(51,20))


# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.

def product(*args):
    result = 1
    for arg in args: 
        result *= arg
    return result

print('Exercise 8:', product(2, 5, 5))
print(product(-1, 4))


# Exercise 9: Basic Calculator
#
# Create a function named `basic_calculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basic_calculator(10, 5, 'subtract') should return 5.
# basic_calculator(10, 5, 'add') should return 15.
# basic_calculator(10, 5, 'multiply') should return 50.
# basic_calculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.

def basic_calculator(n1, n2, operation):
    operation = operation.lower()
    if operation == 'add': return n1 + n2
    elif operation == 'subtract': return n1 - n2
    elif operation == 'multiply': return n1 * n2
    elif operation == 'divide': return n1 / n2
    else: return "invalid operation"


print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
print(basic_calculator(10, 5, 'add')) # should return 15.
print(basic_calculator(10, 5, 'multiply')) # should return 50.
print(basic_calculator(10, 5, 'divide')) # should return 2.
print(basic_calculator(10, 5, 'squared')) # invalid op