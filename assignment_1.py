# Task 1
# Write down a Python program in order to:
# • Read a positive integer number n.
# • Print out a proper message according to the fact that it is an odd or an even value.

n = int(input("Enter a number: "))

if n > 0:
    if n % 2 == 0:
        print(f"{n} is an even number.")
    else:
        print(f"{n} is an odd number.")
else:
    print("Please enter a positive integer.")

# Task 2
# Write down a Python program which:
# • Reads three integer numbers from the keyboard.
# • Displays an appropriate message on screen according to the fact that:
#   o All the three numbers assume the same value
#   o Two (and only two) numbers have the same value
#   o All the three numbers assume a different value

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 == num2 == num3:
    print("All three numbers have the same value.")

elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Two (and only two) numbers have the same value.")

else:
    print("All three numbers have different values.")

# Task 3
# Write down a Python program which reads three real numbers from the keyboard and displays
# the maximum among them, also saying if it corresponds to the first, second or third value
# introduced by the user.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

max_value = num1
max_position = "first"

if num2 > max_value:
    max_value = num2
    max_position = "second"

if num3 > max_value:
    max_value = num3
    max_position = "third"

print(f"The maximum value is {max_value}, and it corresponds to the {max_position} number you entered.")

# Task 4
# Write a Python program working as a simple prefix calculator: the program must read a prefix
# 2expression, consisting of an operator (+, -, *, /) followed by two real numeric operands, then
# display the operation in the standard format and the result of the expression itself.

def perform_operation(operator, number1, number2):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        if number2 != 0:
            return number1 / number2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

expression = input("Enter a prefix expression (e.g., '+ 3 5'): ")

parts = expression.split()

if len(parts) != 3:
    print("Invalid input. Please use the format: <operator> <operand1> <operand2>")
else:
    operator = parts[0]
    number1 = float(parts[1])
    number2 = float(parts[2])

    result = perform_operation(operator, number1, number2)

    print(f"{number1} {operator} {number2} = {result}")

# Task 5
# Write down a Python program which:
# • Reads three real numbers (a, b and c)
# • Checks whether a, b and c may (or may not) represent the sides’ lengths of a triangle. If
# yes, the program must also determine the triangle type, distinguishing among the
# following cases:
#   o Equilateral triangle, a==b==c
#   o Isosceles triangle, a==b!=c or b==c!=a or a==c!=a
#   o Scalene triangle a!=b!=c
#   o Rectangular triangle c*c==a*a+b*b or a*a==b*b+c*c or b*b==a*a+c*c
# Recall that, in any triangle, the length of each side must be smaller than the sum of the lengths of
# the other two sides.
# a<b+c, b<a+c, c<a+b

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        print("Rectangular triangle")
    else:
        print("Scalene triangle")
else:
    print("These sides do not form a valid triangle.")

# Task 6
# Write down a Python program in order to:
# • Read a character.
# • Print out a proper message according to the fact that it is vowel or consonant.

char = input("Enter a character: ")

if len(char) == 1:
    char = char.lower()

    if char in ['a', 'e', 'i', 'o', 'u']:
        print(f"The character '{char}' is a vowel.")
    else:
        print(f"The character '{char}' is a consonant.")
else:
    print("Please enter a single character.")

# Task 7
# Write down a Python program which:
# • Reads year from the keyboard.
# • Displays an appropriate message on screen according to the fact that year is leap year or
# not:
# Tip: Leap year
# All years which are perfectly divisible by 4 are leap years except for century years( years ending
# with 00 ) which is a leap year only it is perfectly divisible by 400. For example: 2012, 2004,
# 1968 etc are leap year but, 1971, 2006 etc are not leap year. Similarly, 1200, 1600, 2000, 2400
# are leap years but, 1700, 1800, 1900 etc are not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Task 8
# Write down a Python program which reads three real numbers from the keyboard and displays
# the roots of a quadratic equation ax2+bx+c=0 where a, b and c are coefficients. This program will
# ask the coefficients: a, b and c from user and displays the roots.

import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

D = b**2 - 4*a*c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif D == 0:
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(D)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")