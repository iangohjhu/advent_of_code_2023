import math
# https://docs.python.org/3/library/re.html
import re

# input_file = "sample_input3.txt"
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

class nodeClass:
    def __init__ (self, name, left, right):
        self.name = name
        self.left = left
        self.right = right


# function(s)

def displayNodes(nodeList):
    for n in nodeList:
        print(n.name, n.left, n.right)

def indexNode(nodeList, nodeName):
    i = 0
    for n in nodeList:
        if n.name == nodeName:
            return n

def followPath(nodeList, name, direction):
    # find the node
    n = indexNode(nodeList, name)
    if n and direction == 'L':
        return n.left
    if n and direction == 'R':
        return n.right
    
# process list
pathList = []
nodeList = []

pathList = [*list[0].strip()] # unpacked

for i in range(2, last_line):
    line = list[i].strip()
    input = re.split(r"=", line)
    nodeName = input[0].strip()
    elements =  re.split(r",",input[1].replace("(","").replace(")",""))
    leftElement = elements[0].strip()
    rightElement = elements[1].strip()
    newNode = nodeClass(nodeName, leftElement, rightElement)
    nodeList.append(newNode)

startNodesList = []

# find the start nodes (end in A)
for n in nodeList:
    m = re.match(r"..A", n.name)
    if m:
        startNodesList.append(n.name)
        

numStartNodes = len(startNodesList)

stepsList =  []
for i in range(numStartNodes):

    # follow Path until end
    end = False
    steps = 0

    print("Start", startNodesList[i])
    
    while not(end):
        steps += 1
        # print(steps)

        # get direction from list
        d = pathList.pop(0)
        # put it at the end
        pathList.append(d)

        # next Node
        startNodesList[i] = followPath(nodeList, startNodesList[i],  d)
        m = re.match(r"..Z", startNodesList[i])
        if m:
            # reached End
            end = True
            print("Steps", steps)
            stepsList.append(steps)

# output
print("now just compute the least common multiple for those invidual steps")
totalSteps = stepsList[0]
for i in range(1, numStartNodes):
    totalSteps = math.lcm(totalSteps, stepsList[i])

print("totalSteps", totalSteps)

