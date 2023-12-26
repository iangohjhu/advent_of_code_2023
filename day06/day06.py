# https://docs.python.org/3/library/re.html
import re

#input_file = "sample_input.txt"
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

class raceClass:
    def __init__ (self, race, time, distance):
        self.race = race
        self.time = time
        self.distance = distance


# function(s) 

def runRace(r):
    print("Running race", r.race, "time", r.time, "distance", r.distance)
    wins = 0
    for holdTime in range(r.time):
        remainingTime = r.time - holdTime # remainingTime
        speed = holdTime
        distance = speed * remainingTime
        if distance > r.distance:
            wins += 1
            
    print("Ways to win", wins)
    return wins

# process list
raceList = []
timesList = []
distanceList = []

for i in range(last_line):
    line = list[i].strip()
    m = re.match(r"Time:\s+", line)
    if m:
        timesList = re.split(r"\s+", re.split(r"Time:\s+", line)[1])

    m = re.match(r"Distance:\s+", line)
    if m:
        distanceList = re.split(r"\s+", re.split(r"Distance:\s+", line)[1])

# add races w Times and Distances
for r in range(0, len(timesList)):
    race = raceClass(r, int(timesList[r]), int(distanceList[r]))
    raceList.append(race)
 
# run each race
productWaysToWin = 1
for r in raceList:
    w = runRace(r)
    if w > 0:
        productWaysToWin = productWaysToWin * w

# output
print("What do you get if you multiply these numbers together?", productWaysToWin)
