# INHERITENCE IN OOPS

class seller:  # BASE CLASS
    def __init__(self, name, product, price):
        self.name = name
        self.product = product
        self.price = price


class distributor(seller):  # CHILD CLASS
    def __init__(self, name, product, paymentType, price):  # Add init()
        self.payment = paymentType
        seller.__init__(self, name, product, price)  # Inherit from base class

    def invoice(self):  #
        print("Shop name: " + self.name, "\nProduct Purchased :" + self.product, "\n Payment Type :" + self.payment,
              "\nRate of the Product:", self.price)


bill = distributor("x Electronics", "LED", "cash", 25000)
bill.invoice()


# MULTIPLE INHERITANCE   2 Base class , 1 child class
class Apartment:
    def __init__(self, Name, Location, No_offlats):
        self.name = Name
        self.address = Location
        self.flats = No_offlats


class Maintenance:
    def __init__(self, WaterBill, Housekeeping, parking):
        self.water = WaterBill
        self.cleaning = Housekeeping
        self.parking = parking


class Flats(Apartment, Maintenance):
    def __init__(self, cost, sqrfeet, Rooms, Name, Location, No_offlats, WaterBill, Housekeeping, parking):
        self.cost = cost
        self.size = sqrfeet
        self.rooms = Rooms
        Apartment.__init__(self, Name, Location, No_offlats)
        Maintenance.__init__(self, WaterBill, Housekeeping, parking)

    def Estimation(self):
        self.net_amount = self.cost + self.water + self.cleaning + self.parking
        print(f"Apartment : {self.name} || Flats Available : {self.flats} || location : {self.address},\n"
              f"No of Rooms : {self.rooms} || Square Feet : {self.size} || Cost of Flat : {self.cost}\n"
              f"Other Charges :\nWater : {self.water}, Cleaning : {self.cleaning}, Parking : {self.parking},\n Grand Total : {self.net_amount}")


total = Flats(6750000, 1800, "2BHK", "G-SQUARE", "Pallavaram,Chennai",
              125, 450, 500, 1000)
total.Estimation()


# MULTILEVEL INHERITANCE
class supermarket():
    def __init__(self, name, address):
        self.name = name
        self.address = address


class category(supermarket):
    def __init__(self, name, address, prod_type):
        supermarket.__init__(self, name, address)
        self.type = prod_type


class payment(category):
    def __init__(self, name, address, prod_type, pro_name, quantity, price):
        category.__init__(self, name, address, prod_type)
        self.productname = pro_name
        self.quantity = quantity
        self.price = price

    def purchase(self):
        self.total = self.quantity * self.price
        print(
            f"Shop Name : {self.name}, Location : {self.address}, Category : {self.type}, Product : {self.productname}, Quantity : {self.quantity}, Price : {self.price} and the total amount is {self.total}")


get_bill = payment(" A to Z supermarket", "chennai", "Beauty", "fogg perfume", 2, 180)
get_bill.purchase()


# HIERARCHICAL INHERITANCE
class Master:
    def __init__(self, course, batch, timeslot):
        self.course = course
        self.batch = batch
        self.timeslot = timeslot
    def stu_data(self):
        return f"Course Name : {self.course} , Batch and Time : {self.batch},{self.timeslot}"
class student1(Master):
    def __init__(self, id1, name1, fees1, course, batch, timeslot):
        super().__init__(course, batch, timeslot)
        self.id1 = id1
        self.name1 = name1
        self.fees1 = fees1
    def stu_data(self):
        return {super().stu_data()},f"ID : {self.id1}, Name : {self.name1}, Fees :{self.fees1}"

class student2(Master):
    def __init__(self, id2, name2, fees2, course, batch, timeslot):
        super().__init__(course, batch, timeslot)
        self.id2= id2
        self.name2 = name2
        self.fees2 = fees2

    def stu_data(self):
        return {super().stu_data()}, f"ID : {self.id2}, Name : {self.name2}, Fees :{self.fees2}"


data1 = student1("ID101", "viswa", 12000,"Python","Batch A","10 AM")
data2 = student2("ID102", "kumar", 10000,"SQL","Batch D","11 AM")
print(data1.stu_data())
print(data2.stu_data())
