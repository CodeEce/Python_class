#1 write a python program to reverse a string "123abcd"
string = input("Enter string")
def reverse_str(string):
    rev = string[::-1]
    print("The string reversed",rev)
reverse_str(string)

# 2. Write a  Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :No. of Upper case characters : 3  ,No. of Lower case Characters : 12

sample_str = input("Enter string")
def str_count(sample_str):
    count = 0
    count1 = 0
    for i in sample_str:
        if i.isupper():
            count += 1
        elif i.islower():
            count1 += 1
    print("No. of Upper case characters :",count,"\nNo. of Lower case Characters :",count1)
str_count(sample_str)

# 3. Write a  Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
sample_list =[1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_num(sample_list):
    even_number = []
    for i in sample_list:
        if i % 2 == 0:
            even_number.append(i)
    print("Even number from the list:",even_number)
even_num(sample_list)

# 4. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
list1=[1,2,3,3,3,3,4,5]
def ret_dist(list1):
    new_list =[]
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    print("The distinct elements from a list is:",new_list)
ret_dist(list1)

# 5. Write a  Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Input : red-orange-blue-black-pineapple
# Output : black-blue-orange-pineapple-red
fruits ="red-orange-blue-black-pineapple"
def sequence(fruits):
    fruit_list = fruits.split("-")
    sorted_list=sorted(fruit_list)
    result ="_".join(sorted_list)
    print("The sorted fruit list separated by hyphen('_'):\n",result)
sequence(fruits)

# 6 Write a  Python function to multiply all the numbers in a list.
num_list = [5,4,10,3]
def multiply(num_list):
    mul =1
    for i in num_list:
        mul*=i
    print("The multiplied value of the number is:",mul)
multiply(num_list)

# 7. Write a  Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)    Expected Output : 20
sum_list = (8,2,3,0,7)
def sum_num(sum_list):
    sum=0
    for i in sum_list:
        sum+=i
    print("The sum value of the number is:",sum)
sum_num(sum_list)

# 8. Write a  Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
num =int(input("enter number"))
def square_list(num):
    new_list = []
    for i in range(1,num+1):
        root= i**2
        new_list.append(root)
    print(new_list)
square_list(num)

# 9. Generate a Python list of all the even numbers between 4 to 30.
ev_num = int(input("Enter the number"))
def even_number(ev_num):
        even_list =[]
        for i in range(4,ev_num):
            if i %2 == 0:
                even_list.append(i)
        print(even_list)

even_number(ev_num)
# 10. How to Print Multiple Arguments in Python?
def my_Data(stu_id,name,course,institution):
     print(f"I am {name} and my id is {stu_id}\n I am studying {course} in {institution}")
my_Data("s124","vinothini","Data Analytics","Besant Technologies")












