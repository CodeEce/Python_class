  # PYTHON STRINGS

x = "  Python, Language!"
y = "Welcome"
z = "to Python"

quotes = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor 'incididunt'
ut labore et dolore magna aliqua."""
print(quotes)

print("Get the character position of 25 is", quotes[25])   # Get position

for name in "Vinothini":     # Looping through a string
    print(name)

print(len(quotes))     # Length of Strings

print("labore" in quotes)    # Check String
print("energy" in quotes)
if "labore" in quotes:
    print("YES,labore is present")

print("constructing" not in quotes)      # Check String if not
print("dolore" not in quotes)
if "constructing" not in quotes:
    print("NO,constructing is not present.")

 # STRING SLICING

print(quotes[2:10])
print(x[:8])                 # slice from start
print(x[0:])                 # slice to end
print(x[-5:-1])              # negative index

 # MODIFY STRINGS

print(x.upper())             # uppercase
print(x.lower())             # lowercase
print(x.strip())             # Remove whitespace
print(x.replace("Language","LANGUAGE"))    # replace the string
print(x.split("a"))                # split the string
print(y+' '+z)                     # space between string

 # CONCATENATE STRINGS
data1 = "Google"
data2 = "Analytics"
concat = data1+data2
print(concat)                   # concatenation
print(data1 + " "+ data2)       # concatenation with space

 # FORMAT STRINGS
age = 25
txt1 = f"My name is john, i am {age}"    # f string
print(txt1)
price = 25
txt2 = f"This price is {price:.2f} dollars"
print(txt2)
txt3 = f"This price is {100*5} dollars"
print(txt3)

 # ESCAPE CHAR

text = "The escape character\ballow\'s you to use \\double quotes\n when you\r normally \twould not be allowed."
print(text)

 # STRING METHODS

news = "weather Report"
ad = news.capitalize()
print(ad)
ad1 = news.casefold()
print(ad1)
ad2 = news.center(100)
print(ad2)
ad3 = news.count("e")
print(ad3)
ad4 = news.encode()
print(ad4)
ad5 = news.endswith("o")
print(ad5)
ad6 = news.expandtabs(10)
print(ad6)
ad7 = news.find("ther")
print(ad7)
ad8 = news.index("weather")
print(ad8)
news1 = "Temperature 28.0 degree"
ad9 = news1.isalnum()
print(ad9)
ad10 = news1.isalpha()
print(ad10)
ad11 = news1.isascii()
print(ad11)
ad12 = news1.isdecimal()
print(ad12)
ad13 = news1.isdigit()
print(ad13)
ad14 = news1.islower()
print(ad14)
ad15 = news1.isnumeric()
print(ad15)
ad16 = news1.isprintable()
print(ad16)
ad17 = news1.isspace()
print(ad17)
ad18 = news1.upper()
print(ad18)
ad19 = news1.title()
print(ad19)
list1 = ("led","speaker","remote")
ad20 = "@".join(list1)
print(ad20)
ad21 = news1.rjust(50)
print(ad21)
ad22 = ad21.ljust(70)
print(ad22)
ad23 = text.splitlines()
print(ad23)
ad24 = text.startswith("I")
print(ad24)
ad25 = text.swapcase()
print(ad25)
ad26 = news.zfill(20)
print(ad26)


 #PYTHON BOOLEANS

value1 = bool(25>10)
print(value1)
print(bool("hello"))
print(bool(25))
print(bool(0))


