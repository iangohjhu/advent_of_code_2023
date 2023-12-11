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

# classes
class Number:
  def __init__(self, x1, y1, x2, y2, value):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.value = value
      
class Gear:
  def __init__(self, x, y, number):
    self.x = x
    self.y = y
    self.number = number


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

def isGear(c):
    if c == '*':
        return True
        
    return False
    
def outputList(listGears):
  # print("List of Gears")

  lastX = -1
  lastY = -1
  lastNum = 0
  gearRatio = 0
  sumGearRatios = 0

  sorted_listGears = sorted(listGears, key=lambda obj: (obj.x, obj.y))
  
  for obj in sorted_listGears:
    print(obj.x, obj.y, obj.number)
    if (lastX == obj.x and lastY == obj.y):
      gearRatio = lastNum * obj.number
      print("gearRatio", gearRatio)
      sumGearRatios += gearRatio

    lastX = obj.x
    lastY = obj.y
    lastNum = obj.number
  
  print("Sum of gear ratios", sumGearRatios)        
      


def gearPos(x,y):

  pos = 0
  for object in listGears:
    if object.x == x and object.y == y:
      return pos
    pos += 1

  # didn't find a gear at x,y
  return -1

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

def checkAdjacentForSymbol(number):

  # print("Checking", number.value, "for adjacent symbol")
  foundSymbol = False
  
  # check top of number
  for x in range(number.x1 -1, number.x2 + 2):
    y = number.y1 - 1
    # print("checkAdjacentForSymbol", x, y)
    if inGrid(x, y):
      if isSymbol(cell(x, y)):
        # print (x, y, cell(x, y))
        # it's a gear so we need to store this gear saw a number
        if isGear(cell(x, y)):
          listGears.append(Gear(x,y, number.value))
        foundSymbol=True
        
  # check bottom of number
  for x in range(number.x1 -1, number.x2 + 2):
    y = number.y1 + 1
    # print("checkAdjacentForSymbol", x, y)
    if inGrid(x, y):
      if isSymbol(cell(x, y)):
        # print (x, y, cell(x, y))
        # it's a gear so we need to store this gear saw a number
        if isGear(cell(x, y)):
          listGears.append(Gear(x,y, number.value))
        foundSymbol=True

  # check left of number
  x = number.x1 - 1
  y = number.y1
  # print("checkAdjacentForSymbol", x, y)
  if inGrid(x, y):
    if isSymbol(cell(x, y)):
      # print (x, y, cell(x, y))
      # it's a gear so we need to store this gear saw a number
      if isGear(cell(x, y)):
        listGears.append(Gear(x,y, number.value))
      foundSymbol=True  

  # check right of number
  x = number.x2 + 1
  y = number.y1
  # print("checkAdjacentForSymbol", x, y)
  if inGrid(x, y):
    if isSymbol(cell(x, y)):
      # print (x, y, cell(x, y))
      # it's a gear so we need to store this gear saw a number
      if isGear(cell(x, y)):
        listGears.append(Gear(x,y, number.value))
      foundSymbol=True   

  return foundSymbol
 

# process input

index = 0
max_row =len(my_data)

array = []

for i in range(0,max_row):
        row = list(my_data[i].strip())
        max_col = len(row)        
        array.append(row)


# check array for valid engine codes

curNumber = 0
x = 0
y = 0
x1 = -1
y1 = -1
x2 = -1
y2 = -1


# creating lists
listGears = []
listNumbers = []

while inGrid(x,y):

    if isDigit(cell(x,y)):
        # print(x, y, cell(x,y))
        curNumber = curNumber * 10 + int(cell(x,y))
        if x1 == -1 or y1 == -1:
          # number begins at x1, y1
          x1 = x
          y1 = y
        # number ends at x2, y2
        x2 = x
        y2 = y
    else:
        if curNumber > 0:
          # print ("Found", x1, y1, x2, y2, curNumber)
          listNumbers.append(Number(x1, y1, x2, y2, curNumber))
          
        # reset before we go on
        curNumber = 0
        x1 = -1
        y1 = -1
        x2 = -1
        y2 = -1
            
    x = x + 1
    
    if (not inGrid(x,y)):
        x = 0
        y = y+1
        # before we go on to the next row, check if we have a curNumber
        if curNumber > 0:
          # print ("Found", x1, y1, x2, y2, curNumber)
          listNumbers.append(Number(x1, y1, x2, y2, curNumber))

        # reset before we go to next line
        curNumber = 0
        x1 = -1
        y1 = -1
        x2 = -1
        y2 = -1

# check numbers for adjacent symbols
sumPartNumbers = 0

for obj in listNumbers:
    # short cut, numbers are horizontal (e.g., y1 = y2)
    # print(obj.x1, obj.y1, obj.x2, obj.y2, obj.value)

    nextToSymbol = False    

    if checkAdjacentForSymbol(obj):
      nextToSymbol = True
        
    if nextToSymbol:
      sumPartNumbers += obj.value
      
# output
print("What is the sum of all of the part numbers in the engine schematic?", sumPartNumbers)

outputList(listGears)
