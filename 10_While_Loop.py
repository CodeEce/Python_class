# WHILE LOOP
i = 10     # REVERSE
while i > 5:
    print(i)
    i -= 1

# ELSE STATEMENT
i = 5
while i < 12:
    print(i)
    i += 1
else:
    print("no more values")

# BREAK STATEMENT
i = 10
while i < 20:
    print(i)
    if i == 15:
        break
    i += 1

# CONTINUE STATEMENT
i = 25
while i < 45:
    i += 1
    if i == 35:
        continue
    print(i)



