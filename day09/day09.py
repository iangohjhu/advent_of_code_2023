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

# init

# classes


# function(s)
def convertLineIntoList(line):
    input = re.split(r"\s", line)
    inputList = []

    for i in input:
        inputList.append(int(i))

    return inputList

def diff(inputList):
    outputList = []

    a = inputList[0]
    for i in range(1, len(inputList)):
        b = inputList[i]
        c = b - a
        a = b
        outputList.append(c)

    return outputList    
        
def allZeros(inputList):
    for i in range(len(inputList)):
        if inputList[i] != 0:
            return False
    return True

def getSequenceList(inputList):
    sequenceList = []

    while not allZeros(inputList):
        sequenceList.append(inputList)
        outputList = diff(inputList)
        inputList = outputList

    # the last would be all zeroes
    sequenceList.append(inputList)
    return sequenceList

def nextNumberInSequence(inputList, diff):
    last = len(inputList) - 1
    next = inputList[last] + diff
    return next


def nextSequenceList(sequenceList):
    # starting from the last sequence, compute the next number in sequence
    for i in range(len(sequenceList) - 1, -1, -1):
        s = sequenceList[i]
        if i == len(sequenceList) - 1:
            diff = 0
        n = nextNumberInSequence(s, diff)
        # use that next number in the next sequence
        diff = n
        # print(s, n)
    return n
    
# process list
sumValues = 0
for i in range(last_line):
    line = list[i].strip()
    inputList = convertLineIntoList(line)
    sequenceList = getSequenceList(inputList)
    v = nextSequenceList(sequenceList)
    sumValues += v

# output
print("sum of these extrapolated values", sumValues)
