# PYTHON SETS

menu = {"cake", "sandwich", "veg roll", "donut"}
price = {30, 25, 25, 20, True, 1,"cake"}
chocolates = {"milkybar","5star", "kitkat"}
beverages = ["orange","milkshake","smoothies"]
print(menu)
print(len(menu))
print(type(menu))

# ACCESS SETS
print(True in menu)
print("veg roll" not in menu)

# ADD SETS
menu.add("samosa")
print(menu)

menu.update(chocolates)
print(menu)
menu.update(beverages)
print(menu)
menu.remove("veg roll")
print(menu)
menu.discard("donut")
print(menu)
items = menu.pop()
print(items)
price.clear()
print(price)
del price

# JOIN SETS

# UNION joins all items on both sets
total_menu = menu.union(chocolates)
print(total_menu)

food_Item = menu.union(chocolates,beverages)
print(food_Item)

chat_Item={"masala puri", "pani puri"}
menu.update(chat_Item)
print(menu)

# INTERSECTION keeps only the duplicates
check_menu = menu.intersection(chat_Item)
print(menu)
print(check_menu)
menu.intersection_update(chat_Item)
print(menu)

# DIFFERENCE keeps the items from the first set that are not in the other set(s)
junk_veg ={"french fries","burger","pop-corn"}
junk_nonveg = {"chicken pizza","burger","popcorn_chicken"}
junk_Items = junk_veg.difference(junk_nonveg)   # store value into new variable
print(junk_Items)
junk_veg.difference_update(junk_nonveg)         # store value into same varilble using update
print(junk_Items)

# SYMMETRIC_DIFFERENCE keeps all items EXCEPT the duplicates
nuts = {"almond","cashew","pista"}
fried_nuts = {"cashew","pista","peanuts"}
nuts_items = nuts.symmetric_difference(fried_nuts)
print(nuts_items)
nuts.symmetric_difference_update(fried_nuts)
print(nuts)

# SETS METHODS

spicy_snacks = {"roasted peanut","chips"}
sweet_items ={"coconutbar","peanutbar"}
x = menu.copy()
print(x)
y = spicy_snacks.isdisjoint(sweet_items)
print(y)
z = nuts_items.issubset(nuts)
print(z)
w = nuts.issuperset(nuts_items)
print(w)
chat_Item.clear()
print(chat_Item)

# LOOP SETS
cloth = {"jean","shirt","maxi"}
for i in cloth:
    print(i)
