import re

# Define the file's name.
filename = "testInput.txt"

# Open the file and read its content.
with open(filename) as f:
    content = f.read().splitlines()

# Display the content.
for index, line in enumerate(content):
    try:
        line = re.split(r"[\.]+", line.strip())
        # line = line.split(',')
        # lineLength = len(line)
        # val = line[0] + line[lineLength - 1]
        content[index] = line
        # print(line)
    except IOError:
        pass
print(content)
