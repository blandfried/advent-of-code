import re

# Define the file's name.
filename = "day2Input.txt"

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

id_vals = []
i = 1
while i <= len(content):
    game_vals = my_games[str(i)]
    isPossibleList = []
    for game in game_vals:
        if len(isPossibleList) == 0:
            isPossibleList.append(
                {
                    "blueMax": game["blue"],
                    "redMax": game["red"],
                    "greenMax": game["green"],
                }
            )
        else:
            if isPossibleList[0]["blueMax"] < game["blue"]:
                isPossibleList[0]["blueMax"] = game["blue"]
            if isPossibleList[0]["greenMax"] < game["green"]:
                isPossibleList[0]["greenMax"] = game["green"]
            if isPossibleList[0]["redMax"] < game["red"]:
                isPossibleList[0]["redMax"] = game["red"]

    i += 1
    for item in isPossibleList:
        id_vals.append(item["blueMax"] * item["greenMax"] * item["redMax"])

print(sum(id_vals))
