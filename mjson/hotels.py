import json

file = open('hotels.json', 'r')
file_contents = json.load(file)
file.close()

data = file_contents['data']

for i in range(len(data)):
    print(f"{i+1} - {data[i]['attributes']['name']} -> in city {data[i]['attributes']['address']['city']}")



