# https://docs.python.org/3/library/re.html
import re

# input_file = "sample_input.txt"
input_file = "puzzle_input.txt"

# open files in read mode
file = open(input_file, 'r')

# read lines in file
data = file.readlines()

# make it a list
list = list(data)

# last line
last_line = len(list)

# close file
file.close()

# max cubes
max_reds = 12
max_greens = 13
max_blues = 14

sum_possible_games = 0

# process list
for line in list:
    m = re.split(r":", line)
    # print (m[0], m[1])
    # m[0] = Game X
    g = re.search(r"Game (\d+)", m[0])
    gameId = int(g.group(1))
    # m[1] = the subsets of cubes shown
    s = re.split(r";", m[1].strip())
    
    # print("Game", gameId)
    # game is possible until proven impossible
    isPossible = True

    for set in s:
        # print(set)
        match_blues = re.search(r"(\d+) blue", set)
        match_reds  = re.search(r"(\d+) red", set)
        match_greens = re.search(r"(\d+) green", set)
        if match_blues:
            # print("blues", match_blues.group(1))
            if int(match_blues.group(1)) > max_blues:
                isPossible=False
        if match_reds:
            # print("reds", match_reds.group(1))
            if int(match_reds.group(1)) > max_reds:
                isPossible=False
        if match_greens:
            # print("greens", match_greens.group(1))
            if int(match_greens.group(1)) > max_greens:
                isPossible=False

    if isPossible:
        print("Game", gameId, "is possible")
        sum_possible_games += gameId
    else:
        print("Game", gameId, "is impossible")

        
# output

print("Sum of the IDs of possible games", sum_possible_games)
