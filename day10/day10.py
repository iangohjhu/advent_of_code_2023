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

# globals
visitedList = []
queueList = []

# classes

class posClass:
  def __init__(self, x, y):
    self.x = x
    self.y = y
               
class mazeClass:
  def __init__(self, pos, d):
    self.pos = pos
    self.distance = d # distance from Start


# function(s)
def maze(pos):
  if inMaze(pos):
    return array[pos.y][pos.x]

def inMaze(pos):
    if pos.x < 0:
        return False
    if pos.y < 0:
        return False
    if pos.x >= max_col:
        return False
    if pos.y >= max_row:
        return False
    return True
  
# . is ground; there is no pipe in this tile.
def isGround(pos):
  if maze(pos) == '.':
    return True

  return False

# | is a vertical pipe connecting north and south.
def isVertical(pos):                  
    if maze(pos) == "|":
        return True

    return False

# - is a horizontal pipe connecting east and west.
def isHorizontal(pos):
    if maze(pos) == '-':
        return True
        
    return False

# L is a 90-degree bend connecting north and east.
def isNE(pos):
  if maze(pos) == 'L':
    return True

  return False

# J is a 90-degree bend connecting north and west.
def isNW(pos):
  if maze(pos) == 'J':
    return True

  return False

# 7 is a 90-degree bend connecting south and west.
def isSW(pos):
  if maze(pos) == '7':
    return True

  return False

# F is a 90-degree bend connecting south and east.
def isSE(pos):
  if maze(pos) == 'F':
    return True

  return False

def isStart(pos):
    if maze(pos) == 'S':
        return True
        
    return False

def findStart():
  for x in range(0, max_col):
    for y in range(0, max_row):
      pos = posClass(x,y)
      if isStart(pos):
        return mazeClass(pos, 0)
      
def bfs(m):

  visitedList.append(m)
  queueList.append(m)
  
  while queueList:
    m = queueList.pop(0)

    # find next
    for m2 in possibleNext(m):
      if not alreadyOnList(visitedList, m2):
          visitedList.append(m2)
          queueList.append(m2)

    
def possibleNext(m):
  pos = m.pos
  dist = m.distance

  # try possible next positions
  nextList = []

  # try up (so long as we're not in the 0 row)
  if pos.y != 0:
    newpos = posClass(pos.x, pos.y - 1)
    if (isVertical(newpos) or isSW(newpos) or isSE(newpos)):
      m = mazeClass(newpos, dist + 1)
      nextList.append(m)

  # try left (so long as we're not in the 0 col)
  if pos.x != 0:
    newpos = posClass(pos.x -1, pos.y)
    if (isHorizontal(newpos) or isNE(newpos) or isSE(newpos)):
      m = mazeClass(newpos, dist + 1)
      nextList.append(m)

  # try right (so long as we're not in max col)
  if pos.x != max_col:
    newpos = posClass(pos.x + 1, pos.y)
    if (isHorizontal(newpos) or isNW(newpos) or isSW(newpos)):
      m = mazeClass(newpos, dist + 1)
      nextList.append(m)

  # try down (so long as we're not in the max row)
  if pos.y != max_row:
    newpos = posClass(pos.x, pos.y + 1)
    if (isVertical(newpos) or isNE(newpos) or isNW(newpos)):
      m = mazeClass(newpos, dist + 1)
      nextList.append(m)

  # for m in nextList:
  #  print("next", m.pos.x, m.pos.y)
    
  return nextList


def displayPath(list):
  # max (so far)
  max = start
  
  for t in list:
    # print(t.pos.x, t.pos.y, t.distance)
    if t.distance > max.distance:
      max = t

  # part one : 7097
  print("Furthest from start", max.pos.x, max.pos.y, "steps", max.distance)
      

def alreadyOnList(list, m):
  # is this pos in the nextList?
  for t in list:
    if t.pos.x == m.pos.x and t.pos.y == m.pos.y:
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

# find the starting point
start = findStart()
      
# initiate a breadth first search from the start
bfs(start)

# output
displayPath(visitedList)
