friends = input("Enter the name of your 3 friends, with comma separated values \n").split(',')
people = open("people.txt",'r')
people_nearby = [line.strip() for line in people.readlines()]

for i in range(len(people_nearby)):
    people_nearby[i] = people_nearby[i].lower()

for j in range(len(friends)):
    friends[j] = friends[j].lower()

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt','w')

for friend in friends_nearby_set:
    nearby_friends_file.write(f"{friend}\n")

nearby_friends_file.close()