# caeser encoder

# removes spaces in ciphertext

#TODO: build testable functions such that a test won't get caught in a while loop

import re

def shifter(shift):
    while True:
        try:
            n = int(shift)
            break
        except ValueError:
            #TODO sub for an exception, vs. print?
            print("Only enter a numeric shift")
    return shift

#TODO refactor to make testable
def plainTextInput():

    while True:
        plainText = input("Enter message, only alphabet no numbers, no punctuation: ")
        plainText.lower()
        result = bool(re.search(r'\d', plainText))
        if result:
            print("Enter message, no numbers, no puntuation.")
        else:
            break

    return plainText


def encoder(shift, plainText, alpha):

    plainList = list(plainText)

    cipherList = []

    for i in range(len(plainList)):
        if plainList[i] == ' ':
            pass
        else:
            plainChar = plainList[i].lower() 
            initIndex = alpha.index(plainChar)
            cipherIndex = initIndex + int(shift)
            if cipherIndex > 25:
                cipherIndex = cipherIndex % 25 - 1
            cipherChar = alpha[cipherIndex]
            cipherList.append(cipherChar)


    cipher = ''.join(cipherList)
    return cipher



def processor(): 
    '''
    all inputs taken here, fed into mutator functions
    - allows testing of individual mutator/processing fxns
    '''

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            

    shiftInput = input("Input shift value: ")
    
    shift = shifter(shiftInput)

    print("Shift chosen:", shift)


    plainText = plainTextInput()

    cipherText = encoder(shift, plainText, alpha)

    print("Original:", plainText)
    print("Shift:", shift)
    print("Cipher Text:", cipherText)

    return cipherText




