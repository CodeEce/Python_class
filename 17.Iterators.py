# ITERATOR
mydata = ("hospital","school","office")
myit = iter(mydata)
print(next(myit))
print(next(myit))
print(next(myit))

data = "memory"
myit = iter(data)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# loop through iterator
for i in mydata:
    print(i)
for i in data:
    print(i)
# Create an iterator that returns numbers, starting with 1
class numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
myclass = numbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# STOPITERATION

class details:
    def __iter__(self):
        self.a =1
        return self
    def __next__(self):
        if self.a <=7:
           x = self.a
           self.a += 1
           return x
        else:
            raise StopIteration
getDet = details()
detit = iter(getDet)
for x in detit:
    print(x)


