import re

# Define the file's name.
filename = "dayInput.txt"

# Open the file and read its content.
with open(filename) as f:
    content = f.read().splitlines()

# Display the content.
for index, line in enumerate(content):
    try:
        line = re.sub(r"[a-z]*", "", line)

        lineLength = len(line)
        val = line[0] + line[lineLength - 1]
        content[index] = int(val)
    except IOError:
        pass
print(sum(content))
