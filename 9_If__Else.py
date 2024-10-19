#  CONDITIONAL STATMENT
#  IF_______ELSE

class_A = 25
class_B = 21
if class_A > class_B:
    print("class_A greater than class_B")

vivo_price = 42999
iphone = 72999
if vivo_price < iphone:
    print("vivo mobile price is lessthan iphone price")
elif vivo_price > iphone:
    print("vivo mobile price is greterthan iphone price")
else:
    print("both price are equal")
# SHORT HAND IF.........
if class_A > class_B: print("class_A is greterthan class_B")
# SHORT HAND IF...ELSE
a = "banana"
b = "lemonooo"
x = len(a)
y = len(b)
print("string length of banana is greater") if x > y else print("string length of lemon is greater")

# USING AND

number1 = 49
number2 = 49
number3 = 42

if number1 > number2 and number3 < number1:
    print("number 1 is greater,so both condition are true")
else:
    print("condition false")
if number1 == number2 or number3 < number1:
    print("one condition satisfied")
else:
    print("both condition failed")
if not len(a) == len(b):
    print("length of a and b not equal")

# NESTED IF
pass_mark = 35
maths = 84
science = 72
english = 43
attend = True

if attend:
    print("Present")
    if maths >= pass_mark and science >= pass_mark and english >= pass_mark:
        print("PASS")
    else:
        print("FAIL")
else:
    print("absent")

if x == y:
    pass




