import re

# Define the file's name.
filename = "day1Input.txt"

# Open the file and read its content.
with open(filename) as f:
    content = f.read().splitlines()

listOne = []
listTwo = []
# Display the content.
for index, line in enumerate(content):
    try:
        lineArray = line.split()
        listOne.append(int(lineArray[0]))
        listTwo.append(int(lineArray[1]))
    except IOError:
        pass

distanceArray = []
for index, itemOne in enumerate(listOne):
    try:
        occurrence = listTwo.count(itemOne)
        distanceArray.append(occurrence*itemOne)
    except IOError:
        pass
print(sum(distanceArray))
