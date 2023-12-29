# https://docs.python.org/3/library/re.html
import re

# input_file = "sample_input.txt"
# needed some better samples
# input_file = "sample_input2.txt"
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

class handClass:
    def __init__ (self, hand, bid):
        self.hand = hand
        self.bid = bid

# function(s) 

def strengthOfCard(card):
    return cardOrder.index(card)

def strengthOfHand(hand):
    return handOrder.index(typeOfHand(hand))

def typeOfHand(hand):
    uniqueCardList = sorted(set(hand), key=strengthOfCard)
    # print("uniqueCards" , uniqueCardList)


    # count each uniqueCard
    countCards = [0 for e in range(len(uniqueCardList))]
    for c in hand:
       countCards[uniqueCardList.index(c)] += 1

    # what's my hand now?
    # print("before Joker", hand, uniqueCardList)
    
    # for c in uniqueCardList:
    #    print(c, countCards[uniqueCardList.index(c)])
        
    # how many jokers?
    countJokers = 0
    if 'J' in uniqueCardList:
        countJokers = countCards[0] # joker will be in pos 0
        # remove Joker from uniqueCardList
        uniqueCardList.remove('J')
        # move up countCards since J was in pos 0
        for i in range(len(countCards) - 1):
            countCards[i] = countCards[i+1]
        
        # add jokers to the uniqueCard that has the highest count + rank
        highestCard = 0
        highestCardCount = 0
        for i in range(len(uniqueCardList)):
            if countCards[i] >= highestCardCount:
                highestCard = i
                highestCardCount = countCards[highestCard]
        countCards[highestCard] += countJokers

    # edge case JJJJJ
    if countJokers == 5:
        # make the card an ACE
        uniqueCardList.append('A')
        countCards[0] = 5
        
    # what's my hand now?
    # print("after Joker", hand, uniqueCardList)
    
    # for c in uniqueCardList:
    #    print(c, countCards[uniqueCardList.index(c)])
    
    for c in uniqueCardList:

        # Five of a kind, where all five cards have the same label: AAAAA
        if countCards[uniqueCardList.index(c)] == 5:
            return("Five of a kind")
        
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        if countCards[uniqueCardList.index(c)] == 4:
            return("Four of a kind")
            
        # Full house, where three cards have the same label, and the remaining two cards share same label: 23332
        if countCards[uniqueCardList.index(c)] == 3 and len(uniqueCardList) == 2:
            return("Full house")
            
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        if countCards[uniqueCardList.index(c)] == 3 and len(uniqueCardList) == 3:
            return("Three of a kind")

    # need to do a bit more counting how many pairs?
    pairs = 0
    for c in uniqueCardList:
        if countCards[uniqueCardList.index(c)] == 2:
            pairs += 1

    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    if pairs == 2:
        return("Two pair")
    
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    if pairs == 1:
        return("One pair")

    # High card, where all cards' labels are distinct: 23456
    if len(uniqueCardList) == 5:
        return("High card")
        
def displayCards(cardList):
    rank = 0
    for h in cardList:
        rank += 1
        print(rank, h.hand, h.bid)

            
def currentHandRankedLower(h1, h2):
    # print("currentHandRankedLower")
    # print(h1, strengthOfHand(h1))
    # print(h2, strengthOfHand(h2))
    if strengthOfHand(h2) < strengthOfHand(h1):
        # print("h2 < h1")
        return True
    if strengthOfHand(h2) == strengthOfHand(h1):
        # hands equally ranked
        # need to compare individual cards
        for i in range(len(h1)):
            if h2[i] == h1[i]:
                # keep comparing
                # print(i, h2[i], "=", h1[i])
                continue
            if cardOrder.index(h2[i]) < cardOrder.index(h1[i]):
                # print(i, h2[i], "<", h1[i])
                return True
            else:
                # print(i, h2[i], ">", h1[i])
                return False
    return False

def totalWinnings(cardList):
    totalWinnings = 0
    rank = 0
    for h in cardList:
        rank += 1
        totalWinnings += (rank * h.bid)

    return totalWinnings

# process list
# pt2 with joker rule
cardOrder = ('J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A')
handOrder =("High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind")
handList = []

for i in range(last_line):
    line = list[i].strip()
    input = re.split(r"\s+", line)
    aHand = [*input[0]] # unpack string 
    theBid = int(input[1])
    hand = handClass(aHand, theBid)
    handList.append(hand)

handListRanked = []

# sort the cardList by rank
for currentHand in handList:
    # print("currentHand", currentHand.hand)
    queue = []
    while len(handListRanked) > 0:
        priorHand = handListRanked.pop()
        if currentHandRankedLower(priorHand.hand, currentHand.hand):
            # current hand is ranked lower so keep going
            # store the priorHand in queue
            queue.append(priorHand)
        else:
            # put back prior hand
            handListRanked.append(priorHand)
            # get out of while loop
            break
        
    # add currentHand
    handListRanked.append(currentHand)

    # push queue onto handListRanked
    while len(queue) > 0:
        priorHand = queue.pop(-1)
        handListRanked.append(priorHand)


# output
print("HandListRanked")           
displayCards(handListRanked)
print("Total winnings", totalWinnings(handListRanked))
