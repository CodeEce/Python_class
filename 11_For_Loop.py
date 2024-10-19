# FOR LOOP
device = ["laptop", "keyboard", "mouse", "mobile", "speaker"]
for items in device:
    print(items)

# Loop through string

for get in "National":
    print(get)

# BREAK STATEMENT
for items in device:
    print(items)
    if items == "keyboard":
        break

for items in device:
    if items == "keyboard":
        break
    print(items)

# CONTINUE STATEMENT
for items in device:
    if items == "keyboard":
        continue
    print(items)

# RANGE FUNCTION
for values in range(15):
    print(values)

start = int(input("Enter start value:"))
end = int(input("Enter end value:"))
increment = int(input("Enter increment value"))
for values in range(start, end, increment):
    print(values)

# ELSE STATEMENT
for values in device:
    print(values)
else:
    print("values are listed")

# NESTED FOR LOOP
brands = ["nykaa", "forest essential", "ponds", "lotus"]
products =["sunscreen", "shampoo", "conditioner"]

for i in brands:
    for j in products:
        print(i, j)

