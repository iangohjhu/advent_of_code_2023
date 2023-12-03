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


# function(s)

def isPossible(subsets):

    for set in subsets:
        # print(set)
        match_blues = re.search(r"(\d+) blue", set)
        match_reds  = re.search(r"(\d+) red", set)
        match_greens = re.search(r"(\d+) green", set)
        
        if match_blues:
            # print("blues", match_blues.group(1))
            if int(match_blues.group(1)) > max_blues:
                return False
        if match_reds:
            # print("reds", match_reds.group(1))
            if int(match_reds.group(1)) > max_reds:
                return False
        if match_greens:
            # print("greens", match_greens.group(1))
            if int(match_greens.group(1)) > max_greens:
                return False

    # if we get this far, subsets were possible
    return True

# process list
for line in list:
    m = re.split(r":", line)
    # print (m[0], m[1])
    # m[0] = Game X
    g = re.search(r"Game (\d+)", m[0])
    gameId = int(g.group(1))
    # m[1] = the subsets of cubes shown
    subsets = re.split(r";", m[1].strip())
    
    # print("Game", gameId)
    # game is possible until proven impossible

    if isPossible(subsets):
        print("Game", gameId, "is possible")
        sum_possible_games += gameId
    else:
        print("Game", gameId, "is impossible")

        
# output

print("Sum of the IDs of possible games", sum_possible_games)
