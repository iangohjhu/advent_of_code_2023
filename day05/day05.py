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
seedsList = []
mapsTuple = ('seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:')
indexSection = -1
mapsLookup = []

# classes

class seedClass:
    def __init__ (self, number):
        self.number = number
        self.data = []

    def add(self, map, value):
        self.data.append([map, value])        
        
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

def mapSeeds(index, mapsLookup, seedsList):
    # Each line within a map contains three numbers: the destination range start, the source range start, and the range length.
    for s in seedsList:
        v = lookupSeed(mapsLookup, s.number)
        s.add(index, v)
        s.number = v

def displaySeeds(seedsList):
    lowest = 0
    lowestLocation = -1
    for s in seedsList:
        initialSeed = -1
        for d in s.data:
            if d[0] == -1:
                initialSeed = d[1]
                print("seed", initialSeed)
            else:
                 print(mapsTuple[d[0]], d[1])
            if d[0] == 6:
                # location
                if (lowestLocation == -1) or d[1] < lowestLocation:
                    lowest = initialSeed
                    lowestLocation = d[1]
                
    print("lowest location number", lowestLocation)
                    
# process list
for i in range(last_line):
    line = list[i].strip()
    m = re.match(r"seeds:\s+", line)
    if m:
        for s in re.split(r"\s+", re.split(r"seeds:\s+", line)[1]):
            newSeed = seedClass(int(s))
            seedsList.append(newSeed)
    newIndex = parseListSection(line)
    if (indexSection < newIndex) or (i == last_line -1):
        # do seed mapping before we move on?
        mapSeeds(indexSection, mapsLookup, seedsList)
        # in a new section
        indexSection = newIndex
        mapsLookup = []
    m = re.match(r"^[\d]+ [\d]+ [\d]+", line)
    if m and indexSection > -1:
        # print(mapsTuple[indexSection], m[0])
        mapsLookup.append(re.split(r"\s+", line))

# output
displaySeeds(seedsList)
