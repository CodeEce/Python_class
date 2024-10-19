# Python List
listItem = ["apple", "banana", "cherry", "banana", 24, 2.24, True]  # Allow duplicate values and multipe datatypes
vegTuple = ("potato", "brinjal")
x = listItem.count("banana")
print(x)
print(listItem)
print(listItem[2])  # index
print(listItem[-1])
print(len(listItem))  # length
print(type(listItem))  # typeof

stationary = list(("pen", "Notebook"))  # list() constructor
print(stationary)
print(listItem[2:4])
print(listItem[-3:-1])
if "banana" in listItem:
    print("Yes banana is in the list")
listItem[2] = "mango"
print(listItem)
listItem[3:4] = ["kiwi", "lemon"]
print(listItem)

listItem.insert(3, "strawberry")  # add new item using position
print(listItem)
stationary.insert(2, "scale")
print(stationary)

stationary.append("eraser")  # add new item to the list (single value)
print(stationary)

listItem.extend(stationary)
print(listItem)

stationary.extend(vegTuple)
print(stationary)

stationary.remove("brinjal")  # remove particular item using value
print(stationary)
stationary.pop(2)  # remove particular item using index value
print(stationary)
stationary.pop()  # Remove last item
print(stationary)
del stationary[0]  # Remove first item
print(stationary)
listItem.clear()  # empty list
print(listItem)
#  del listItem
#  print(listItem)       # show error ,listItem deleted

mylist = listItem.copy()
print(mylist)

print(listItem)
print(mylist)

brands = ["volvo", "renault", "bmw"]
model = ["i10", "i20", "kia"]

brands[2] = ["maruti", "suzuki", "bajaj"]
print(brands)
print(brands[2][2])

# JOIN LIST
list1 = ["apple","mango","Banana","strawberry"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list2.extend(list1)
print(list2)

# SORT LIST
#sort list alphanumericaly

list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
list4 = [5,2,4,9,7,25,0,3.58]
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)
fruits = ["Guava","grapes","Litchi"]
fruits.sort()
print(fruits)
fruits.sort(key = str.lower)
print(fruits)
fruits.reverse()
print(fruits)

# LOOP LIST
mobile = ["apple","samsung","vivo"]
for x in mobile:
    print(x)
# Loop through index number
gadgets = ["headset", "charger", "adapter"]
for x in range(len(gadgets)):
    print(gadgets[x])
# using while loop
i = 0
while i < len(gadgets):
    print(gadgets[i])
    i += 1
# looping using list comprehension
cooler =["venus", "everest","kenstar"]
[print(get_list) for get_list in cooler]


















