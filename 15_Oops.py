# CLASS / OBJECTS
class my_class:  # Create class
    x = 25


obj = my_class()  # Create object
print(obj.x)


# __init__() Function
class vehicle:
    def __init__(car_data, brand, model, price):
        car_data.brand = brand
        car_data.model = model
        car_data.price = price


sale = vehicle("honda", "pleasure", 25000)
print(sale.brand)
print(sale.model)
print(sale.price)


# __str__() Function:
class student:
    def __init__(data, name, age):
        data.stu_name = name
        data.age = age

    def __str__(self):
        return f"{self.stu_name},{self.age}"


obj = student("vino", 27)
print(obj)


# OBJECT Methods

class employee:
    def __init__(emp, name, designation):
        emp.emp_name = name
        emp.emp_designation = designation

    def emp_function(self):
        print(self.emp_name, self.emp_designation)


empObj = employee("vino", "developer")
empObj.emp_function()

empObj.emp_name = "Manoj"  # modify object properties
print(empObj.emp_name)

del empObj.emp_designation  # delete object properties
print(empObj.emp_designation)

# del empObj  # delete objects
print(empObj)
