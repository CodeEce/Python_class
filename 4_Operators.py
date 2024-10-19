# PYTHON OPERATORS
# Arithmetic Operator
num1 = 14
num2 = 6
print("Addition of two numbers", num1 + num2)
print("Subtraction of two numbers", num1 - num2)
print("Multiplication of two numbers", num1 * num2)
print("Division of two numbers", num1 / num2)
print("Modulus of two numbers", num1 % num2)
print("14 power 6 is", num1 ** num2)
print("Floor division value is", num1 // num2)

# Assignment Operator
num3 = 4
print(num3)
num3 += 6
print("num3 += is", num3)
num3 -= 6
print("num3 -= is", num3)
num3 *= 6
print("num3 *= is", num3)
num3 /= 6
print("num3 /= is", num3)
num3 %= 6
print("num3 %= is", num3)

# Comparision Operator
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

# Logical Operator
print(10 > num1 < 20)        # num1 = 14 , num2 = 6
print(10 > num2 or num2 < 20)
print(not (10 > num1 < 20))

# Identity Operator
fruits = ["apple","Orange"]
vegetables = ["potato","Ginger"]
organic = vegetables
print(fruits is vegetables)
print(vegetables == organic)
print(fruits is not vegetables)
print(organic != vegetables)

# Membership Operator
print("orange" in fruits)
print("mango" not in fruits)

# Bitwise Operator
print(4 & 6)        # AND (1 & 1 = 1) otherwise 0
print(4 | 6)        # OR  (0 | 0 = 0) otherwise 1
print(4 ^ 6)        # XOR (both 1,1 = 0 and both 0,0 = 1 otherwise 0)
print(~3)           # NOT (0 becomes 1 , 1 becomes 0)

