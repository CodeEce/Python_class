
# LIST COMPREHENSION
subject = ["tamil","english","maths","science"]
new_list = []
for x in subject:
    if "e" in x:
        new_list.append(x)
print(new_list)

add_list = [x for x in subject if "a" in x]
print(add_list)

s = [y for y in subject if y != "maths"]
print(s)

# ITERABLE
e = [x for x in range(5)]
print(e)
t = [x for x in range(10) if x<8]
print(t)
p = [x.upper() for x in subject]
print(p)
# SET VALUE
c = ["computer" for x in subject]
print(c)
z = [x if x != "science" else "computer" for x in subject]
print(z)