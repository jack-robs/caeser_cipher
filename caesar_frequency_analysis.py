
testCipher = 'abbcccddddeeeee'

#TODO create standard freq dict

def freqAnalysis():
    
    freqDict = {}

    freqList = list(testCipher)

    for i in range(len(freqList)):
        if freqList[i] in freqDict:
            freqDict[freqList[i]] += 1
        else:
            freqDict[freqList[i]] = 1


    return freqDict
