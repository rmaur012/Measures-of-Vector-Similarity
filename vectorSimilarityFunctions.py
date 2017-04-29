#This python file contains all the measures of vector similarity between word co-occurrance vectors v and w

from math import sqrt

def simCosine(v, w):
	numeratorSum = 0
	vVectorSum = 0
	wVectorSum = 0
	

	for index,value in enumerate(v):
		numeratorSum = numeratorSum + (value * w[index])
		vVectorSum = vVectorSum + (value * value)
		wVectorSum = wVectorSum + (w[index] * w[index])
	
	denominatorTotal = (sqrt(vVectorSum) * sqrt(wVectorSum))

	similarity = numeratorSum/denominatorTotal

	return similarity


def simJaccard(v, w):
    numeratorMinSum = 0
    denominatorMaxSum = 0

    for index, value in enumerate(v):
        if value <= w[index]:
            numeratorMinSum = numeratorMinSum + value
        else:
            numeratorMinSum = numeratorMinSum + w[index]

        if value >= w[index]:
            denominatorMaxSum = denominatorMaxSum + value
        else:
            denominatorMaxSum = denominatorMaxSum + w[index]

    similarity = numeratorMinSum / denominatorMaxSum

    return similarity



def simDice(v, w):
    numeratorMinSum = 0
    denominatorSum = 0

    for index, value in enumerate(v):

        if value <= w[index]:
            numeratorMinSum = numeratorMinSum + value
        else:
            numeratorMinSum = numeratorMinSum + w[index]

        denominatorSum = denominatorSum + (value + w[index])

    similarity = ((2 * numeratorMinSum) / denominatorSum)

    return similarity

#To be implemented later with more information
#def simJS(v, w):
#        similarity = 0

#        return similarity

