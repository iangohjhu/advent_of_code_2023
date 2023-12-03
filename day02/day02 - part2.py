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


# function(s)

def power(subsets):

    min_blues = 0
    min_reds = 0
    min_greens = 0
    
    for set in subsets:
        # print(set)
        match_blues = re.search(r"(\d+) blue", set)
        match_reds  = re.search(r"(\d+) red", set)
        match_greens = re.search(r"(\d+) green", set)
        
        if match_blues:
            # print("blues", match_blues.group(1))
            if int(match_blues.group(1)) > min_blues:
                min_blues = int(match_blues.group(1))
        if match_reds:
            # print("reds", match_reds.group(1))
            if int(match_reds.group(1)) > min_reds:
                min_reds = int(match_reds.group(1))
        if match_greens:
            # print("greens", match_greens.group(1))
            if int(match_greens.group(1)) > min_greens:
                min_greens = int(match_greens.group(1)) 

    # return the power of the set of minimum cubes
    power = min_blues * min_reds * min_greens
    return power

# sum
sum_of_powers = 0

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
    # print( power(subsets) )
    sum_of_powers += power(subsets) 
    
        
# output

print("The sum of the power of these sets:", sum_of_powers)
