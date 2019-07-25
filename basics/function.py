players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]


#void function, in python it will returm "None" if eveluated


def printNameAndNumber(player):
    print(f"{player['name']} has got  {sumOfNumber(player['numbers'])}")


#return function


def sumOfNumber(numbers):
    return sum(numbers)


# if first argument has a default value then all subsequesnt paraneters should have a default values
def add(a=1, b=2):
    return a+b


for i in range(len(players)):
    printNameAndNumber(players[i])

print(add())#3
print(add(5, 5))#10






