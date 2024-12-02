import re

# Define the file's name.
filename = "dayInput.txt"

# Open the file and read its content.
with open(filename) as f:
    content = f.read().splitlines()

numbersMap = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
ks = numbersMap.keys()

# Display the content.
for index, line in enumerate(content):
    try:
        x = re.findall(
            r"(?=(one|two|three|four|five|six|seven|eight|nine))",
            line,
        )
        xLen = len(x)
        if xLen > 0:
            newNumWord = x[0].replace(x[0][1], numbersMap[x[0]])
            line = line.replace(x[0], newNumWord)
            line = numbersMap[x[xLen - 1]].join(line.rsplit(x[xLen - 1], 1))
        line = re.sub(r"[a-z]*", "", line)
        lineLength = len(line)
        val = line[0] + line[lineLength - 1]
        content[index] = int(val)
    except IOError:
        pass
print(sum(content))
