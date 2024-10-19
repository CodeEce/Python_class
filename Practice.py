# ---------------------------------------------- Add 2 numbers---------------------------------
# Add Two Numbers with “+” Operator
import math

num1 = 10
num2 = 20
num3 = num1 + num2
print("Addition of two numbers :", num3)

# Add Two Numbers with User Input
num1 = input("Enter number")
num2 = input("Enter a number")
sum = float(num1) + float(num2)
print("sum of {0} and {1} is:{2}".format(num1, num2, sum))


# Add Two Numbers in Python Using Function
def addNum(a, b):
    return a + b
num1 = 10
num2 = 8.5
sum = addNum(num1, num2)
print("sum of {0} and {1} is : {2}".format(num1, num2, sum))

# Add Two Numbers Using operator.add() Method
import operator

num1 = 5
num2 = 20
sum = operator.add(num1, num2)
print(sum)

# Add Two Number Using Lambda Function
sumOf_two = lambda x, y: x + y
num1 = 10
num2 = 75
result = sumOf_two(num1, num2)
print(result)


# Add Two Numbers Using Recursive Function
def rec_Add(a, b):
    if b == 0:
        return a
    else:
        return a + b
num1 = 28
num2 = 47
sum = rec_Add(num1, num2)
print(sum)
# ------------------------------------------- Find Maximum number--------------------------
# Find Maximum of two numbers in Python
def maximum(a,b):
    if a>= b:
        return a
    else:
        return b
num1 = 10
num2 =9.9
max = maximum(num1,num2)
print("The MAX num is : ",max)

# Find Maximum of two numbers Using max() function
a = 2
b = 4
maximum = max(a, b)
print(maximum)

# Maximum of two numbers Using Ternary Operator
x = 78
y = 68
print(x if x>=y else y)

# Maximum of two numbers Using lambda function
x = 20
y= 10
sum = lambda x,y: x if x>=y else y
print(sum(x,y))

# Maximum of two numbers Using list comprehension
x=2;y=10
a = [x if x>=y else y]
print(a)

# Maximum of two numbers Using sort() method
x = 10
y = 74
a = [x,y]
a.sort()
print(a[-1])

# --------------------------------------------- Find Factorial -----------------
# Simple Python program to find the factorial of a number
n = 6
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"Factorial of {n} is",fact)

# Get Factorial of a Number using a Recursive Approach
def findFact(n):
    return 1 if n==1 or n == 0 else n * findFact(n-1)
n = 8
print(findFact(n))

# Factorial Function in Maths
import math
def fact(n):
    return math.factorial(n)
num = 5
print(fact(num))

# Python Program for simple interest
p = int(input("Entet the Principal Amount: "))
r = int(input("Enter Rate of Interest : "))
t = int(input("Enter Tennure period"))
def simpleint(p,r,t):
    si = (p * r * t)/100
    return si
print(simpleint(p, r, t))

# Python Program for Compound Interest
def compound(p,r,t):
    Amount = p*(1+r/100)**t
    ci = Amount - p
    return ci
p = 3000
r = 5
t = 3

print(compound(p,r,t))

#Compund interest using loop
def cint(p,r,t):
    amount = p
    for i in range(t):
        amount =amount*(1+r/100)
    CI = amount -p
    return CI
p = 2000
r = 2
t = 3
print(cint(p,r,t))

# Python Program to check Armstrong Number
num = int(input("Enter number"))
count = len(str(num))
sum = 0
temp = num
while temp >0:
    x = temp % 10              # 153 % 10 = 3 to get last digit
    sum =sum + (x**count)
    temp = temp //10           # 153 // 10 = 15  to get second last digit
if sum == num:
    print("Amstrong Number")
else:
    print("Not An Amstrong Number")

# Python Program to Find Area of a Circle
pi = 3.14
r = 8
Area = pi * (r**2)
print("Tha Area of Circle is :",Area)

import math
def findarea(r):
    area = math.pi*pow(r,2)
    return area
print(findarea(2))

# To Find  Circumference Of Circle
def circum(r):
   c =2*math.pi*r
   return c
print(circum(4))

# Python Program for Prime Number or not
lst = []
num = 25
flag = False
if num == 1:
    print("1,is not a prime number")
elif num>1:
    for i in range(2,num):
       if num % i == 0:
        flag = True
        lst.append(i)
print(lst)
if flag:
    print("It's not a prime number")
else:
    print("it,s a prime number")

# Python Program for n-th Fibonacci number
n = 10
a = 0
b = 1
def fib(n):
   if n < 0:
      print("incorrect input")
   elif n == 0:
       return a
   elif n == 1:
       return b
   else:
       f = fib(n-1) + fib(n-2)  # 0 1 = 1 + 1= (2 +(3) =  (5) + (8) = 13 )+21 34 55
       return f
print(fib(n))

# Python Program for How to check if a given number is Fibonacci number?
import math
n = 20
def ispersqr(x):
    s = int(math.sqrt(x))
    return s*s == x
def isfib(n):
    return ispersqr(5*n*n + 4) or ispersqr(5*n*n -4)
for i in range(1,n):
      if (isfib(i) == True):
          print(i,"is a Fibonacci number")
      else:
        print(i," is Not a Fibonacci number")

# Find ASCII
n = "a"
ascii =ord(n)
print("a = ",ascii)

# Python Program for Sum of squares of first n natural numbers
n = 5
sum = 0
for i in range(1,n+1):
    sum +=(i*i)
print(sum)

# Python Program for cube sum of first n natural numbers
n = 5
sum = 0
for i in range(1,n+1):
    sum += i*i*i
print(sum)