#           INTERVIEW QUESTION
import random

# 1.Python program to check if the input number is odd or even ?
check_num = int(input("Enter a number"))
if check_num % 2 == 0:
    #print("The given number is Even")
    print("{0} is Even".format(check_num))
else:
    print("{0} is Odd".format(check_num))

# USING FUNCTION
check_num = int(input("Enter a number"))
def ev_od(check_num):
    if check_num % 2 ==0:
        print(check_num,"is EVEN")
    else:
        print(check_num,"is ODD")
ev_od(check_num)

#  2 .Palindrome Program( String) using inbuilt Method ?
word = input("Enter a string")
if word == word[::-1]:
   print(word,"is a palindrome")
else:
   print(word,"is Not a palindrome")

# USING FUNCTION
word = input("Enter a string")
def palindrome(word):
    if word == word[::-1]:
        print(word, "is a palindrome")
    else:
        print(word, "is Not a palindrome")
palindrome(word)

# 3. Python program to find largest ?
num = [10,15,102,38,75]
get_max = max(num)
print("The largest number from a list is:",get_max)

# USING FUNCTION
num = [35,10,24,89,999]
def max_num(num):
    max = num[0]
    for i in num:
        if i > max:
           max = i
    print("The Largest number from a list is:",max)
max_num(num)

# 4. Python Program to Check Leap Year ?
Year = int(input("Enter a year"))
if Year % 400 == 0 and Year % 100 == 0:
    print(f"{Year} is a Leap Year ")
elif Year % 4 ==0 and Year % 100 != 0:
    print(f"{Year} is a leap year")
else:
    print(f"{Year} is not a leap year")


# 5. Find the Factorial of a Number ?
from math import factorial
num = int(input("Enter a number to find factorial"))
if num == 0 or num ==1:
    print(f"Factorial of {num} is 1")
else:
   print(num * factorial(num-1))

# USING FUNCTION
num = int(input("Enter a number to find factorial"))
def factorial(n):
    if n == 0 or n == 1:
       return 1
    else:
       return n * factorial(n - 1)
print(f"Factorial of {num} is {factorial(num)}")

# 6. Generating a Random number ?
import random
random_num = random.randint(0,50)
print("Random number between 1 to 50:\n",random_num)


# 7 . Find a even number ?
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399,
           162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67,
           104, 58, 512,24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
even_number = []
for i in numbers:
    if i % 2 == 0:
        even_number.append(i)
print("Even numbers from the list:\n",even_number)

# 8 .Function to demonstrate printing pattern ?
n = int(input("Enter a row"))
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end = " ")
        print("\r")
pattern(n)

# FULL PYRAMID
row = int(input("Enter a number"))
def tri_pyramid(row):
    for i in range(1, row + 1):
        for j in range(row - i):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print("*", end=" ")
        print()
tri_pyramid(row)

# REVERSE PYRAMID
row = int(input("Enter a number"))
def tri_pyramid(row):
    for i in range(row,0,-1):
        for j in range(row - i):
            print(" ", end=" ")
        for k in range(2 * i -1):
            print("*", end=" ")
        print()
tri_pyramid(row)

# 9.Program to display the Fibonacci sequence ?
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

# 10 . Program to check if a number is prime or not
num = int(input("Enter the number"))
flag = False
if num == 1:
    print(" 1 is not a prime number")
elif num>1:
    for i in range(2,num):
        if num % i == 0:
            flag =True
            break
        print(i)
if flag:
    print("It's not a prime number")
else:
    print("It,s a prime number")


