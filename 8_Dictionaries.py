# PYTHON DICTIONARIES
student_Info = {"Id":"ID401", "Name" : "Harjith", "age":21,"sex":"male"}
subjects = {"sub1":"physics", "sub2":"maths", "IT":["network","AI"]}
print(len(student_Info))
print(subjects["sub2"])
print(type(subjects))

# ACCESS ITEMS
details = student_Info["Name"]
print(details)
details = student_Info.get("age")
print(details)
details = student_Info.keys()
print(details)
details = student_Info.values()
print(details)

subjects["sub3"] = "chemistry"
print(subjects)
details = subjects.items()
print(details)
if "name" in student_Info:
    print("YES")

# CHANGE ITEMS and ADD ITEMS

student_Info["blood group"] = "A+"
print(student_Info)
student_Info.update({"blood group":"B-ve"})
print(student_Info)

# REMOVE ITEMS

student_Info.pop("sex")
print(student_Info)
student_Info.popitem()
print(student_Info)
del subjects["sub3"]
print(subjects)
#del subjects
#student_Info.clear()
print(student_Info)

# COPY ITEMS

x = student_Info.copy()
y= dict(subjects)
print(y)
print(x)

# NESTED DICTIONARIES
company_xy = {
    "employee1": {"EID": "e01", "name": "pooja", "designation": "Developer"},
    "employee2": {"EID": "e02", "name": "ruba", "designation": "Manager"},
    "employee3": {"EID": "e03", "name": "raja", "designation": "Accounts"}
             }
print(company_xy)

album1 = {"name": "lizzaa", "year": 2012}
album2 = {"name": "snow", "year": 2014}
music_album = {
    "album1": album1,
    "album2": album2
}
print(music_album)

# Access item in nested dictionaries

print(company_xy["employee1"]["designation"])

# DICTI0NARY METHODS

language = ('python', 'java', 'angular')
y = 0
program = dict.fromkeys(language, y)
print(program)

bike = {
  "brand": "pulsar",
  "model": "abs",
  "year": 2001
}
ride = bike.setdefault("model", "avenger")
print(ride)

# LOOP THROUGH DICT

plants = {"name":"tulsi","type":"herbs"}
for i in plants:
    print(plants[i])
for i in plants.keys():        # GET KEYS
    print(i)
for i in plants.values():      # GET VALUES
    print(i)
for i in plants.items():       # GET ITEMS
    print(i)





















