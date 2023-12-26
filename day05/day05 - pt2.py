# https://docs.python.org/3/library/re.html
import re

# input_file = "sample_input.txt"
input_file = "puzzle_input6.txt"

print(input_file)

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
seedsList = []
mapsList  = []
mapsTuple = ('seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:')
indexSection = -1

# classes

class seedClass:
    def __init__ (self, s, r):
        self.start = s
        self.range = r  

class mapClass:
    def __init__ (self, i, m):
        self.index = i
        self.map   = m
        
# function(s) 

def parseListSection(line):
    if line in mapsTuple:
        # match
        return mapsTuple.index(line)

    # no match
    return -1

def lookupSeed(mapsLookup, seedValue):
    # default if no mapping
    lookup =  seedValue

    for map in mapsLookup:
        destStart = int(map[0])
        srcStart = int(map[1])
        range = int(map[2])
        if srcStart <= seedValue and seedValue <= srcStart + range -1:
            # in this range
            lookup = destStart + (seedValue - srcStart)
            # print(seedValue,"in", map[0], map[1], map[2], "maps to", lookup)
    return lookup


                    
# process list
mapsLookup = []
 
for i in range(last_line):
    line = list[i].strip()
    m = re.match(r"seeds:\s+", line)
    if m:
        # seeds are now in a range
        pairsList = re.split(r"\s+", re.split(r"seeds:\s+", line)[1])
        maxPairs  = int(len(pairsList) / 2)
        for i in range(maxPairs):
            seedStart = int(pairsList[2*i])
            seedRange = int(pairsList[2*i + 1])
            newSeed = seedClass(seedStart, seedRange)
            seedsList.append(newSeed)
    newIndex = parseListSection(line)

    m = re.match(r"^[\d]+ [\d]+ [\d]+", line)
    if m and indexSection > -1:
        # print(mapsTuple[indexSection], m[0])
        mapsLookup.append(re.split(r"\s+", line))

    if (indexSection < newIndex) or (i == last_line -1):
        # store seed map before we move on
        # mapSeeds(indexSection, mapsLookup, seedsList)
        newMap = mapClass(indexSection, mapsLookup)
        mapsList.append(newMap)        
        # in a new section
        indexSection = newIndex
        mapsLookup = []


    
# process seeds
lowestSeed = 0
lowestLocation = -1

for s in seedsList:
    for initialSeed in range(s.start, s.start + s.range - 1):
        v = initialSeed
        for m in mapsList:
            # print(m.index, m.map)
            v = lookupSeed(m.map, v)

        # the final v should be the location
        if (lowestLocation == -1) or v < lowestLocation:
            lowestSeed = initialSeed
            lowestLocation = v
            # output
            print("lowest seed", lowestSeed)
            print("lowest location number", lowestLocation)


