# https://docs.python.org/3/library/re.html
#import re

# input_file = "sample_input.txt"
# input_file = "sample_input2.txt"
input_file = "puzzle_input.txt"

# open files in read mode
file = open(input_file, 'r')

# read lines in file
my_data = file.readlines()

# close file
file.close()

# function(s)
def cell(x,y):
    return array[y][x]

def isDigit(c):
    digits = {'0', '1', '2', '3', '4', '5', '6', '7','8', '9'}
                  
    if c in digits:
        return True

    return False

def isPeriod(c):
    if c == '.':
        return True

    return False

def isSymbol(c):                  
    if isDigit(c) or isPeriod(c):
        return False

    return True

def inGrid(x,y):
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= max_col:
        return False
    if y >= max_row:
        return False
    return True

def checkAdjacentForSymbol(x,y):
    for x1 in (x -1, x, x + 1):
        for y1 in (y -1, y, y + 1):
            # print("checkAdjacentForSymbol", x1, y1)
            if inGrid(x1, y1):
                if isSymbol(cell(x1, y1)):
                    # print (x1, y1, cell(x1, y1))
                    return True

    return False

# process input

index = 0
max_row =len(my_data)

array = []

for i in range(0,max_row):
        row = list(my_data[i].strip())
        max_col = len(row)        
        array.append(row)


# check array for valid engine codes

x = 0
y = 0
curNumber = 0
adjacentSymbol = False
sumPartNumbers = 0

while inGrid(x,y):

    if isDigit(cell(x,y)):
        # print(x, y, cell(x,y))
        curNumber = curNumber * 10 + int(cell(x,y))
        # check for adjacent symbol
        adjacentSymbol = adjacentSymbol or checkAdjacentForSymbol(x, y)
        # print("adjacentSymbol", adjacentSymbol)
        
    if isSymbol(cell(x,y)) or isPeriod(cell(x,y)):
        # print(x, y, cell(x,y), curNumber, adjacentSymbol)
        # check if we found a number
        if curNumber > 0:
            if adjacentSymbol or isSymbol(cell(x,y)):
                print ("Found", curNumber)
                sumPartNumbers += curNumber
        # reset before we go on
        curNumber = 0
        adjacentSymbol = False
            

        
    x = x + 1
    
    if (not inGrid(x,y)):
        x = 0
        y = y+1
        # before we go on to the next row, check if we have a curNumber
        if curNumber > 0 and adjacentSymbol:
            print ("Found", curNumber)
            sumPartNumbers += curNumber
        # reset before we go to next line
        curNumber = 0
        adjacentSymbol = False
                
# output
print("What is the sum of all of the part numbers in the engine schematic?", sumPartNumbers)
