# import random 
#     # import the random module

# print(random.randrange(1,10))
#     # used random() within the range of 1-9

fullname = " Maria Kutappa "

print(fullname.upper())
print(fullname.lower())
print(fullname.strip())
print(fullname.replace("M", "P"))
print(fullname.split(" "))

fname = "juswa"
allowance = 2500
print("Kawawa ka naman", fname)
print("Kawawa ka naman" + fname)
print(f"Kawawa ka naman {fname}, ang allowance ay per month ay {float(allowance):.2f}")

studentList = ["Juswa", "Menard", "Francisco Francisca", "AngelBert", "Vinicu"]
print(studentList[1:4])
print(len(studentList))
studentList[2] = "Macayan"
studentList.append("Makmak")
print(studentList)
studentList.remove("Macayan")
studentList.sort(reverse= True)
print(studentList)

grocerySet = {"cherry", "durian", "apple", "banana"}
for x in grocerySet:
    print(x)

grocerySet.remove("cherry")
print(grocerySet)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

y = car["model"]
z = car.get("brand")
a = car.values()
b = car.items()

print("Model:", y)
print("Brand:", z)
print("Values:", a)
print("As Items:", b)

x = car.keys()
print(x)

car["color"] = "white"
print(x)