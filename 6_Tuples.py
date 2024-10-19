# TUPLES

furniture = ("cot","table","chair")
print(furniture)
print(len(furniture))
print(type(furniture))
x = furniture.count("cot")
print(x)
print(furniture[1])
print(furniture[-1])
print(furniture[0:1])

# UPDATE TUPLES
store = list(furniture)
store[2] = "bed"
furniture=tuple(store)
print(furniture)

# ADD
addNew =list(furniture)
addNew.append("pillow",)
furniture = tuple(addNew)
print(furniture)

appliances = ("fridge","stove")
furniture += appliances
print(furniture)
food = list(furniture)
food.remove("fridge")
furniture = tuple(food)
print(furniture)


(wood, synthetic, *plywood) = furniture
print(wood)
home = furniture+appliances
print(home)
my_tuple = appliances * 2
print(my_tuple)

# LOOP TUPLES
fabric = ("linen","cotton","silk")
for x in fabric:
    print(x)
for i in range(len(fabric)):
    print(fabric[i])

i = 0
while i < len(fabric):
    print(fabric[i])
    i +=1
