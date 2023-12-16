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
    print("Card", cardId, winningTuple, numbersList)

    matches = 0
    for i in numbersList:
        if i in winningTuple:
            print("match", i)
            matches += 1

    value = 0
    if (matches > 0):
        value = 2**(matches -1)
    print("value", value)
    return value
    
totalCardPoints = 0

# process list
for line in list:
    totalCardPoints += readCard(line)

# output
print("How many points are they worth in total",  totalCardPoints)
