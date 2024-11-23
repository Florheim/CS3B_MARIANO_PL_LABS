# "Python activity points out life"
# MARIANO, Florheim CS3B

FirstName = "Florheim Wizard"
MiddleName = "Villena"
LastName = "Mariano"
Address = "Villa Quirino, San Esteban, Ilocos Sur"
Age: 22
FavNumOne = 164
FavNumTwo = 313
Animals =["crowl","Octopus", "Cat"]

actor_one ="Ang gwapo gwapo ko diba? friend MakMak"
actor_two = 'Thank you!"Macayan-puyot"'


actor_oneL = len(actor_one)
actor_twoL = len(actor_two)
addressL = len(Address)

print("My Name is ",FirstName,MiddleName,LastName)
print("Address: " + Address)
print("My Two Favorite Numbers are: " ,FavNumOne,FavNumTwo)
print("My Favorite Animals are: " ,Animals)

print(actor_one, actor_two)
print(actor_one[0])

result = (actor_oneL + actor_twoL)- addressL
print(result)
