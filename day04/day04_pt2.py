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

def readCard(line):

    # get rid of multiple spaces
    line = re.sub(r" +", r" ", line.strip())

    c = re.search(r"Card (\d+):", line)
    cardId = int(c.group(1))
    w = re.search(r": ([\d,\s]+) \|", line)
    winningTuple = tuple(re.split(r" ", w.group(1)))
    l = re.search(r"\| ([\d,\s]+)", line)
    numbersList = re.split(r" ",l.group(1))
    print("Processing Card", cardId)

    matches = 0
    for i in numbersList:
        if i in winningTuple:
            # print("match", i)
            matches += 1

    return matches
    

# process list of cards

# this will hold the number of each card i
arrayCards = []
arrayCards = [1 for i in range(last_line+1)]

# this will hold the nmumber of matches for card i
arrayMatches = []
arrayMatches = [0 for i in range(last_line+1)]

# get matches for each card
for i in range(1, last_line + 1):
    m =  readCard(list[i-1])
    arrayMatches[i] = m

# print(arrayMatches)    
 
# bonus cards
for i in range(1, last_line + 1):
    # the next arrayMatches[i] cards gets arrayCards[i] bonus cards
    for j in range(arrayMatches[i]):
        arrayCards[i + j + 1] +=  arrayCards[i]

# output
totalCards = 0
for i in range(1,last_line+1):
    totalCards += arrayCards[i]
    
print("How many total scratchcards",  totalCards)
