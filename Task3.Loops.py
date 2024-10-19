# FOR LOOPS
# 1.Python program to print all the even numbers within the given range.
s = int(input("Enter the starting value : "))
e = int(input("Enter the ending value : "))
for number in range(s, e):
    if number % 2 == 0:
        print("Even number", number)

# 2. Python program to calculate the sum of all the odd numbers within the given range.
x = int(input("Enter the starting value : "))
y = int(input("Enter the ending value : "))
total = 0
for odd in range(x, y):
    if odd % 2 != 0:
        total += odd
print("sum of odd number:", total)

# 3. Python program to count the total number of digits in a number.
calc = input("Enter the multiple digit number:")
digit = str(calc)
count = 0
for i in digit:
    count += 1
print("Total number of digits:", count)

# 4. Python program that accepts a string and calculates the number of digits and letters.
x = input("Enter the value")  # vino123
digits = 0
letters = 0
for i in x:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
print("The number of digit is ", digits, "and the number of letters is", letters)

# 5. Write a program that takes an integer number and outputs all the even numbers starting from 0 to the number
integer = int(input("Enter the number:"))
for i in range(integer):
    if i % 2 == 0:
        print(i)

# WHILE LOOP

# 1. Write a program that takes an integer number and outputs all the even numbers starting from 0 to the number.
num = int(input("enter the number:"))
i = 0
while i <= num:
    if i % 2 == 0:
        print(i)
    i += 1

# 2. Write a program that takes integers from the user and returns the average. Use a while loop and
# make negative numbers the stop criteria.
sumInt = 0
count = 0
while True:
    integer = int(input("Enter a positive Integer to get the average(Enter negative number to exit)"))
    if integer < 0:
        break
    sumInt = sumInt + integer
    count += 1
total = sumInt / count
print(f"The average of the integer is: {total:.2f}")
# 56 78 24 90 29
####################################################
# 1 .Calculate sum of all numbers from 1 to  given number
number = int(input("Enter a number"))
total = 0
for n in range(0, number):
    n += 1
    total += n
print("Sum values of a given number is:",total)

# 2. Display number from a list using loop
listOf_number = [10,20,30,40]
for x in range(len(listOf_number)):
    print(listOf_number[x])

# 3. Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by 5 ,if the number is greater than 150,then skip it and move to the next number
# if the number is greater than 500 then stop the loop
num_list = [52, 285, 25, 48, 100, 155, 875,40]
for x in range(len(num_list)):
    if num_list[x] % 5 == 0:
        if num_list[x] > 150:
            continue
        elif num_list[x] > 500:
            break
        print("These numbers only satisfied the condition:", num_list[x])

# 4 . Calculate the cube of all numbers from 1 to a given number
given_number = int(input("Enter a number:"))
cube_root = 0
for x in range(1,given_number+1):
    cube_root = x**3
    print(f"The cube value of {x} is",cube_root)































