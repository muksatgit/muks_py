# for loop

listOfTupple = [("Mukesh",39), ("Sarab", 37), ("Vikas",36),("Saurabh",40)]
listOfDictionary = {"Mukesh":39, "Sarab": 37, "Vikas":36,"Saurabh":40}

print("----------------------------------")
for name,age in listOfTupple:
    print(f"{name} is {age} years old")
print("----------------------------------")
for name in listOfDictionary:
    print(name)

print("----------------------------------")
for iName, iAge in listOfDictionary.items():
    print(f"{iName} is {iAge} years old")

print("----------------------------------")

for i in range(10):
  print(i)




