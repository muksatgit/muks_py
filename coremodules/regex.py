import re


price = "Price: SEK 1865.00"
expression = "Price: SEK ([0-9]*\.[0-9]*)"

matches = re.search(expression, price)
print(matches.group(0))
print(matches.group(1))

