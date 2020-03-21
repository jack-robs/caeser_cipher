#test for caesar_encoder
import caesar_encoder


#TODO plainTest I/O no test for yet, has print not exception in caesar_encoder.plainTextInput()
def testEncoderPass(shiftExp, cipherExp, plainTextExp, failedTest, alpha, testNum):
    '''
    Test successful caesar_encoder.encoder()
    shift: shift value to test with
    cipherExp: expected cipher output
    plainTextExp: expected plaintext input
    '''
    print("\n******TEST", testNum, "*******\n")
    returnedShift = caesar_encoder.shifter(shiftExp)
    
    if returnedShift != shiftExp:
        failedTest['shift Input/Output: '] += 1

        print("Input Shift:", str(shiftExp))
        print("******FAILED*******") 
        print("Output Shift:", str(returnedShift))
    else:
        print("Input Shift:", str(shiftExp))
        print("Output Shift:", str(returnedShift))

    
    returnedCipher =  caesar_encoder.encoder(shiftExp, plainTextExp, alpha)
    if returnedCipher != cipherExp:
        failedTest['Cipher Input/Output: '] += 1

        print("Input Cipher:", cipherExp)
        print("******FAILED*******") 
        print("Output Cipher:", returnedCipher)
    else:
        print("Input Cipher:", cipherExp)
        print("Output Cipher:", returnedCipher)
    


def main():

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            
    failedTest = {'shift Input/Output: ': 0,'plaintext Input/Output: ': 0, 'cipher output: ': 0}

    #Test1 - expected Shift 3, PT: Dog, Cipher: grj
    shift1 = 3
    pt1 = 'Dog'
    ct1 = 'grj'
    testNum = 0

    testEncoderPass(shift1, ct1, pt1, failedTest, alpha, testNum)

    print("\n####Final Test Results:####\n")
    for k in failedTest:
        print('Test Results: ' + k + ' ' + str(failedTest[k]))

main()