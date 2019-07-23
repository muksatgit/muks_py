cars = ["ok","ok","ok","faulty","ok"]
i = 0

print("-------Break-----------")
for status in cars:
    i = i+1
    if status == "faulty":
        print(f"{i} Stoping the production line as we have an {status} car here")
        break
    print(f"{i} This car is {status}, please ship it to customer")

i = 0
print("-------Continue-----------")

for status in cars:
    i = i + 1
    if status == "faulty":
        print(f" {i} Skiping the process for this car as we have an {status} car here")
        continue
    print(f" {i} This car is {status}, please ship it to customer")