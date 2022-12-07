"""
Make multiple functions that will return the sum, difference, modulus, product, quotient, and the exponent respectively.

Please use the following function names:

addition = add

multiply = multiply

division = divide (both integer and float divisions are accepted)

modulus = mod

exponential = exponent

subtraction = subt

Note: All math operations will be: a (operation) b
"""

def add(a,b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def mod(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def subt(a, b):
    return a  - b

"""
# Testing Cases
test.assert_equals(add(1, 2), 3)
test.assert_equals(multiply(4, 2), 8)
test.assert_equals(divide(9, 2), 4.5)
test.assert_equals(mod(15, 2), 1)
test.assert_equals(exponent(5, 2), 25)
test.assert_equals(exponent(2, 3), 8)
test.assert_equals(subt(5, 9), -4)
"""
