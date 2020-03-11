# caeser encoder
# removes spaces in ciphertext

import re

def shifter():
    while True:
        shift = input("Input shift value: ")
        try:
            n = int(shift)
            break
        except ValueError:
            print("Only enter a numeric shift")
    return shift

def plainTextInput():

    while True:
        plainText = input("Enter message, only alphabet no numbers: ")
        plainText.lower()
        result = bool(re.search(r'\d', plainText))
        if result:
            print("Enter message, no numbers")
        else:
            break

    return plainText


def encoder(shift, plainText, alpha):
    plainList = list(plainText)

    print("List of plain text:", plainList)


    cipherList = []

    for i in range(len(plainList)):
        if plainList[i] == ' ':
            print('blank')
            pass
        else:
            plainChar = plainList[i].lower() 
            initIndex = alpha.index(plainChar)
            cipherIndex = initIndex + int(shift)
            if cipherIndex > 25:
                cipherIndex = cipherIndex % 25 - 1
            print("Converting", plainChar, "at position", initIndex, "to position", cipherIndex)
            cipherChar = alpha[cipherIndex]
            cipherList.append(cipherChar)


    cipher = ''.join(cipherList)
    return cipher



def processor(): 

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            
    shift = shifter()
   
    print("Shift chosen:", shift)


    plainText = plainTextInput()
    print("Plain text:", plainText)

    cipherText = encoder(shift, plainText, alpha)
    print("Original:", plainText)
    print("Shift:", shift)
    print("Cipher Text:", cipherText)
    return cipherText




