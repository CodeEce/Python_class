# Modules
import math

import Practice
x = Practice.patient["name"]
print("Patient name",x)

import platform
x = dir(platform)
print(x)

from Practice import calculation
Practice.calculation(2,3,5)

# DATE
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%h"))
print(x.strftime("%H"))
y = datetime.datetime(2020, 5, 17,12,24,13)
print(y)

# Python Math
import math
x = math.sqrt(84)
print(x)
y = min(22,21,20)
z = min(22,21,20)
s = math.ceil(-2.7)
c = math.floor(3.7)
p = math.pi

print(y,z,s,c,p)

# JSON
import json
# convert json to dict
data = '{"color":"red","taste":"sweet"}'
x = json.loads(data)
print(x)

# convert dict to json
data1 = {"taste":"sweet","color":"red"}
y = json.dumps(data1)
print(y)

# REgEX
import re
txt = "The world is most beautiful"
x = re.search("^The.*beautiful$",txt)
y = re.findall("ul",txt)
print(x)
print(y)
