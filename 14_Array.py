# ARRAY in Python
vehicle = ["bike","cycle","car","bus"] # Access the element of array
print(vehicle[1])
vehicle[1] = "lorry"  # Modify
print(vehicle)
x = len(vehicle)    # length of array
print(x)
for x in vehicle:   # loop in array
    print(x)
vehicle.append("train")   # add element
vehicle.pop(0)              # Remove element
vehicle.remove("bus")
x = vehicle.copy()
print(x)
y = vehicle.count("bike")
print(y)
air_travel =["helicopter","aeroplane","jet"]
vehicle.extend(air_travel)
print(vehicle)

s = vehicle.index("bus")
print(s)

vehicle.insert(2,"scooter")
print(vehicle)
vehicle.reverse()
print(vehicle)
vehicle.sort()
print(vehicle)
vehicle.clear()


