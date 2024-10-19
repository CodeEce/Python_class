#  1 Write a program to accept percentage from the user and display the grade according to the following criteria:
# Marks  >90  ----> Grade A
# Marks  80 and <= 90 ---> Grade B
# Marks  >= 60 and <= 80 ---> Grade C
# Marks  below 60 ----> Grade D

marks = int(input("Enter the percentage:"))
if marks > 90:
    print("Grade 'A'")
elif marks >= 80 and marks <= 90:
    print("Grade 'B'")
elif marks >= 60 and marks <= 80:
    print("Grade 'C'")
else:
    print("Grade 'D'")

# 2 .Write a program to check whether a person is eligible for voting or not. (voting age >= 18)
age = int(input("enter the age : "))
if age >= 18:
    print("This person eligible for voting")
else:
    print("The person not eligible for voting")

# 3 Write a program to find the lowest number out of two numbers excepted from user.
number1 = int(input("Enter the number 1:"))
number2 = int(input("Enter the number 2:"))
if number1 < number2:
    print("number 1 is lowest number")
else:
    print("number 2 is lowest number")

# 4 Write a program to check whether a number is even or odd.
number = 102
if number % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")

# 5 Write a program to find the largest number out of three numbers excepted from user.
num1 = int(input("Enter the number :"))
num2 = int(input("Enter the number:"))
num3 = int(input("Enter the number:"))
if num1 > num2 and num1 > num3:
    print("num1 is largest number")
elif num2 > num3 and num2 > num1:
    print("num2 is largest number")
elif num3 > num1 and num3 > num2:
    print("num3 is largest number")

# 6 Write a program to accept two numbers and mathematical operators and perform operation accordingly.Output :
# Enter First Number: 7  ,# Enter Second Number: 9 ,# Enter operator : + ,# Your Answer is: 16
x1 = int(input("Enter First Number:"))
x2 = int(input("Enter second Number:"))
operator = input("Enter operator:")

if operator == "+":
    print(x1 + x2)
elif operator == "-":
    print(x1 - x2)
elif operator == "*":
    print(x1 * x2)
elif operator == "/":
    print(x1 / x2)

# 7  Write a program to whether a number (accepted from the user ) is divisible by 3 and 2 both.
getnum = int(input("Enter the number"))
if getnum % 3 == 0 and getnum % 2 == 0:
    print(f"The number {getnum} is divisible by both 3 and 2")
else:
    print(f"The number {getnum} is not divisible by both 3 and 2")

# 8  Accept the number of days from the user and calculate the charge for library according to following:
# Till five days: Rs 2/day.   Six to ten days : Rs 3/day.    11 to 15 days : Rs 4/day.     After 15 days: Rs 5/day

days = int(input("Enter number of days:"))
if days <= 5:
    print(f"The Library Charge is Rs:{days * 2} for {days} days")
elif 6 <= days <= 10:
    print(f"The Library Charge is Rs:{(days - 5)*3 + (5*2)} for {days} days")
elif 11 <= days <= 15:
    print(f"The Library Charge is Rs:{(days - 10)*4 + 5*(2+3)} for {days} days")

elif days > 15:
    print(f"The Library Charge is Rs:{(days - 15)*5 + 5*(2+3+4)} for {days} days")

