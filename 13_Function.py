# PYTHON FUNCTION

# Create function
def school(name, location, contact_number):
    print("Name of the School :", name, "\nAddress: ", location, "\nContact us :", contact_number)
school("SRM Matriculation", "Guduvanchery", 9854236145)
school("Vidhya Mandir Matriculation", "Pallavaram", 654235145)
school("Vels Matriculation", "chrompet", 8421663547)

# arbitary arguments
def books(*author):
    print("The books written by author:", author[1])
books("Jane auston", "Arundathi Roy", "Ayn Rand")

# keyword as an arguments
def products(brand1,brand2,brand3):
    print("products",brand1)
products(brand1="LGE",brand2="samsung",brand3="sony")

# arbitary keyword **arguments
def sea(**fish):
    print("The Name of the fish",fish["fish1"])
sea(fish1="golden",fish2="star")

# DEFSULT PARAMETER VALUE
def toys(name="car"):
   print("The toys i like is" , name)
toys("dora")
toys()

# PASSING LIST AS AN ARGUMENTS
list_OTT =["hotstar","amazon","zee5"]
def OTT(list_OTT):
    for x in list_OTT:
      print(x)
OTT(list_OTT)

# RETURN VALUES
def calculation(a,b,c):
    return a+b*c
print(calculation(1,4,7))

# RECURSION
num =int(input("Enter the number to find factorial:"))
def fact(num):
    if num==0 or num == 1:
        return 1

    else:
        return num * fact(num - 1)
print(f"The factorial of {num} = ",fact(num))


# LAMBDA FUNCTION
operation = lambda a,b,c:a*b/c
print(operation(2,5,3))

# Position only arguments
def my_function(x,/):
    print(x)
my_function(10)
def my_function(x):
    print(x)
my_function(x=10)
# Keyword only arguments
def my_function(*,x):
    print(x)
my_function(x=10)

# Combined positional and keyword arguments
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)


# RECURSION
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)


# python progran to find largest number list1 = [10,20,4,45,99]
list1 =[10,20,4,45,99]
def large_number(list1):
    max = list1[0]
    for i in list1:
       if i>max:
           max=i
    print("Largest number from the list is:",i)
large_number(list1)









