# Python Data Types & Type Conversion

# Numbers
number = 5
print(number, "is a typeof ",type(number))

# Strings
weather = "sunny"
print(weather, "is a typeof", type(weather))

# Float
decimal = 3.425
print(decimal, "is a typeof", type(decimal))

# Complex
expression = 1+2j-1
print(expression, "is a typeof", type(expression))

# List
fruits = ["papaya", "mango", "orange"]
print(fruits, "are a typeof", type(fruits))

# Tuple
items = ("pencil", "book", "pen")
print(items, "are a typeof", type(items))

# Dictionaries
studentDetails = {"name": "Manojh", "age": 20}
print("The student details is a typeof", type(studentDetails))

# Set
carBrand = {"kia", "i20", "BMW"}
print("These Brands are a typeof", type(carBrand))

# Boolean
x = True
print(x, " is a typeof", type(x))

# Type Conversion

num = 25.124    # float
print("The decimal number", num, "is a typeof", type(num))

convertInt = int(num)    # float into int
print("The decimal number", num, "is converted into",convertInt, ",is a typeof", type(convertInt))

convertStr = str(convertInt)     # int into str
print("Now the integer", convertInt, "is converted into string",convertStr, ",is a typeof", type(convertStr))








