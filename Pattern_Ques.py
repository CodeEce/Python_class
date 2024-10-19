# FULL PYRAMID
n = 8
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()

# REVERSE FULL PYRAMID
n = 7
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i -1):
        print("*",end=" ")
    print()


# HALF PYRAMID
n = 5
for i in range(0,n+1):
    for j in range(i+1):
        print("*",end=" ")
    print()

# REVERSE HALF PYRAMID
n = 5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# DIAMOND
num = 5
for i in range(num):
    print(' '*(num-i-1)+'* '*(i+1))
for j in range(num-1,0,-1):
    print(' '*(num-j)+'* '*(j))

# NUMERICAL FULL PYRAMID
s = 5
for i in range(1,s+1):
    for j in range(s-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print(k,end=" ")
    print()

# NUMERICAL HALF PYRAMID
num = 5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# ALPHABET FULL PYRAMID
s = 6
alpha = 65
for i in range(0,s):
    print(" " * (s -i),end=" ")
    for j in range(0,i+1):
        print(chr(alpha),end=" ")
        alpha += 1
    alpha = 65
    print()

# ALPHABET HALF PYRAMID
alp = 65
num = 5
for i in range(0,num):
    for j in range(0,i+1):
        print(chr(alp),end=" ")
    alp += 1
    print()

