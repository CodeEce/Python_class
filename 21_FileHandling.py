# Read Files
s = open("Text.txt","r")
print(s.read())

s = open("C:\\Users\HP\PycharmProjects\pythonProject\Text.txt","r")
print(s.readline(24))
print(s.readline())

x = open("Text.txt","a")
print(x.write("Text.txt"))

# Create\Write files

a = open("Text.txt","a")
a.write("\nHi,Good morning")
a.close()
z = open("Text.txt","r")
print(z.read())

# Delete File
import os
os.remove("Text2.txt")

# Decorators -- Using Function as an argument
def up_text(text):
    return text.upper()

def low_text(text):
    return text.lower()
def greet(func):
    # storing the function in a variable
    greeting = func("Hi, Good morning")
    print(greeting)

greet(up_text)
greet(low_text)