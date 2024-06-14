# Task 1
# Write down a Python program in order to:
# • read a positive integer number n.
# • read n integer numbers from the keyboard.
# • compute and display the average of the n values introduced by the user.

n = int(input("Enter a positive integer n: "))

if n > 0:
    total = 0
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        total += num

    average = total / n
    print(f"The average of the {n} numbers is: {average}")
else:
    print("Please enter a positive integer (n > 0).")

# Task 2
# Write down a Python program which:
# • reads a positive integer number n.
# • computes and displays the nth partial sum of the harmonic series: H(n) = 1 + 1/2 + ... + 1/n

n = int(input("Enter a positive integer n: "))

partial_sum = 0.0

for i in range(1, n + 1):
    partial_sum += 1 / i

print(f"The {n}th partial sum of the harmonic series is: {partial_sum}")

# Task 3
# Write down a Python program able to:
# • read a sequence of integer numbers, terminated by the introduction of a zero.
# • compute the sum of all the positive and, separately, all the negative numbers among the ones
# which have been introduced.
# • display the two values obtained in this way.

positive_sum = 0
negative_sum = 0

while True:
    num = int(input("Enter an integer (0 to quit): "))

    if num == 0:
        break

    if num > 0:
        positive_sum += num
    else:
        negative_sum += num

print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")

# Task 4
# Write down a Python program in order to print a table reporting the decimal value of the ASCII code
# used for representing each letter (both small and capital) in the English alphabet. The
# 'a' 97 'A' 65
# table must be composed of 26 rows and 4 columns, where for each row a small letter, its ASCII
# code, the corresponding capital letter and its ASCII code are specified.

lowercase_letter = ord('a')
uppercase_letter = ord('A')

print('Lowercase  |  ASCII code  |  Uppercase  |  ASCII code')

for letter in range(26):
    lowercase_l = chr(lowercase_letter + letter)
    uppercase_l = chr(uppercase_letter + letter)
    lowercase_ascii = ord(lowercase_l)
    uppercase_ascii = ord(uppercase_l)
    print(f"     {lowercase_l}     |     {lowercase_ascii}     |     {uppercase_l}     |     {uppercase_ascii}")

# Task 5
# Write down a Python program which:
# • reads two positive integer numbers x and y.
# • computes the value of the greatest common divider (gcd) between x and y.
# • prints out such a value.
# Recall that the greatest common divider between two numbers x and y is the largest integer value v
# dividing both x and y perfectly, i.e., producing a remainder equal to 0.
# In order to solve this problem, use the Euclid’s method, which consists of the following steps:
# 1. given x and y, denote with M and m the maximum and minimum values between them,
# respectively
# 2. let r be the remainder of the division between M and m: r =M % m
# 3. if r is equal to 0, then m is the gcd we are looking for
# 4. if r is not equal to 0, then go back and repeat from point 2, replacing the values of M and m
# with m and r, respectively

x = int(input("Enter the first positive integer (x): "))
y = int(input("Enter the second positive integer (y): "))

if x < y:
    smaller = x
else:
    smaller = y

gcd = 1

for i in range(2, smaller + 1):
    if x % i == 0 and y % i == 0:
        gcd = i

print(f"The greatest common divisor (GCD) of {x} and {y} is {gcd}.")

# Task 6
# Write down a Pyhton program which:
# • reads a positive integer number n
# • reads n integer values and:
# o displays the message “ascending sequence” if every number of the sequence
# (beyond the first one) is larger than the previous one
# o displays the message “descending sequence” if every number of the sequence
# (beyond the first one) is smaller than the previous one
# o displays the message “neither ascending nor descending sequence” if
# none of the two conditions above is satisfied

n = int(input("Enter a positive integer n: "))

is_ascending = True
is_descending = True

prev_num = int(input("Enter the first number: "))

for i in range(1, n):
    num = int(input(f"Enter number {i + 1}: "))

    if num < prev_num:
        is_ascending = False

    if num > prev_num:
        is_descending = False

    prev_num = num

if is_ascending:
    print("ascending sequence")
elif is_descending:
    print("descending sequence")
else:
    print("neither ascending nor descending sequence")

# Task 7
# Implement a Python program for:
# • reading an integer number n, with value at least equal to 2.
# • reading n real values from the keyboard.
# • determining the two largest values among these ones, displaying them (in any order).

from random import sample
n = int(input("Enter a number which is higher or equal to 2: "))

real_numbers = list(range(100))
randomized_numbers = sample(real_numbers, k=n)
print("The list of randomized numbers:", randomized_numbers)

randomized_numbers.sort()
sorted_num = randomized_numbers.pop()
sorted_num2 = randomized_numbers.pop()
print("The largest two numbers:", sorted_num2, sorted_num)