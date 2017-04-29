#This is a test of the functions

from vectorSimilarityFunctions import *
from math import ceil

def roundToNearestThousandth(rawNumber):   #Helper function to help shorten the results of the similarities

    rounded = ceil(rawNumber*1000) / 1000
    return rounded

def runThroughAllMeasures(vV, vW):
    print("The similarity measures will be conducted...")

    cosineResult = simCosine(vV, vW)

    print("The Cosine Similarity is:", roundToNearestThousandth(cosineResult))

    jaccardResult = simJaccard(vV, vW)

    print("The Jaccard Similarity is:", roundToNearestThousandth(jaccardResult))

    diceResult = simDice(vV, vW)

    print("The Dice Similarity is:", roundToNearestThousandth(diceResult))

#Run 1: 10 values that are either 1 or 0
vectorV = [1,0,1,0,0,1,0,0,1,0]
vectorW = [1,1,1,1,1,0,1,1,1,1]

print("We have the following vectors: ")
print(vectorV)
print(vectorW)

runThroughAllMeasures(vectorV, vectorW)

#Run 2: 17 values that are single digit each
vectorV = [4,1,4,7,0,4,7,0,4,0,0,4,8,0,4,7,0]
vectorW = [6,2,6,0,7,0,0,8,3,2,7,0,3,1,5,2,0]

print("We have the following vectors: ")
print(vectorV)
print(vectorW)

runThroughAllMeasures(vectorV, vectorW)

#Run 3: 17 values that can be
vectorV = [1,7,0,16,35,16,0,0,52,0,15,8,0,0,0,5,32]
vectorW = [8,10,34,50,29,33,59,0,57,0,13,24,0,53,7,0,0]

print("We have the following vectors: ")
print(vectorV)
print(vectorW)

runThroughAllMeasures(vectorV, vectorW)

