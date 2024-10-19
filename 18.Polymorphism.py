# POLYMORPHISM : multiple classes with the same method name
class food:
    def __init__(self,menu,price):
        self.menu = menu
        self.price = price
    def review(self):
        print("delicious meals")
class snacks:
    def __init__(self,menu,price):
        self.menu = menu
        self.price = price
    def review(self):
        print("crunchy chips")
class drinks:
    def __init__(self,menu,price):
        self.menu = menu
        self.price = price
    def review(self):
        print("tasty drink")

Food = food("meals",120)
Snack = snacks("chips",25)
Drinks = drinks("slice",60)
for x in (Food,Snack,Drinks):
    x.review()

# Polymorphism in inheritance
class costume:
    def __init__(self,gender,age):
        self.gender = gender
        self.age = age
    def cloths(self):
        print("designer")
class kids(costume):
    def cloths(self):
        print("boy")
class adults(costume):
    def cloths(self):
        print("Women")
child = kids("male",5)
adult =adults("women",23)

for i in (child,adult):
    print(i.gender)
    print(i.age)
    i.cloths()

