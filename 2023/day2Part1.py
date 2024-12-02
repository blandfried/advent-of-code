import re

# Define the file's name.
filename = "day2TestInput.txt"

# Open the file and read its content.
with open(filename) as f:
    content = f.read().splitlines()

my_games = {}

# Display the content.
for index, line in enumerate(content):
    try:
        line = line.split(":")
        line[0] = re.sub(r"[^\d]", "", line[0])
        id = line[0].strip()
        val = line[1].strip()
        vals = val.split(";")
        items_list = []
        for index, cube in enumerate(vals):
            items = {"blue": 0, "red": 0, "green": 0}

            for cube_vals in cube.split(","):
                if "blue" in cube_vals:
                    val = re.sub(r"[^\d]", "", cube_vals)
                    items["blue"] = int(val)
                elif "green" in cube_vals:
                    val = re.sub(r"[^\d]", "", cube_vals)
                    items["green"] = int(val)
                elif "red" in cube_vals:
                    val = re.sub(r"[^\d]", "", cube_vals)
                    items["red"] = int(val)
            items_list.append(items)
            my_games[id] = items_list

    except IOError:
        pass
red_limit = 12
green_limit = 13
blue_limit = 14

id_vals = []
i = 1
while i <= len(content):
    game_vals = my_games[str(i)]
    isPossibleList = []
    for game in game_vals:
        if (
            game["blue"] <= blue_limit
            and game["red"] <= red_limit
            and game["green"] <= green_limit
        ):
            isPossibleList.append(1)
        else:
            isPossibleList.append(0)

    if 0 not in isPossibleList:
        id_vals.append(i)
    i += 1

list_to_sum = list(dict.fromkeys(id_vals))
print(sum(list_to_sum))
