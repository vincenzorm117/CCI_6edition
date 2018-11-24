#!/usr/local/bin/python3

def EnglishInt(number):
    if number == 0:
        return 'zero'
    
    if 1000000000000 <= number:
        raise 'Number too large'

    numsL20 = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eightteen','nineteen','twenty']
    tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    powers = ['hundred','thousand','million','billion','trillion']

    def HundredWord(number):
        word = ''
        if 100 <= number:
            hundredDigit = int(number / 100)
            word += numsL20[hundredDigit] + ' hundred '

        tensNum = number % 100
        if 20 <= tensNum:
            tensDigit = int(tensNum / 10)
            word += tens[tensDigit]
            onesNum = tensNum % 10
            if 0 < onesNum:
                word += ' ' + numsL20[onesNum]
        elif 0 < tensNum:
            word += numsL20[tensNum]
        
        return word

    word = '' 
    if 1000000000 <= number:
        curr = int((number % 1000000000000) / 1000000000)
        temp = HundredWord(curr)
        if temp != '':
            word += temp + ' billion '
        
    if 1000000 <= number:
        curr = int((number % 1000000000) / 1000000)
        temp = HundredWord(curr)
        if temp != '':
            word += temp + ' million '
    
    if 1000 <= number:
        curr = int((number % 1000000) / 1000)
        temp = HundredWord(curr)
        if temp != '':
            word += temp + ' thousand '
    
    curr = number % 1000
    temp = HundredWord(curr)
    if temp != '':
        word += temp

    return word


testcases = [
    1,
    23,
    456,
    7890,
    12345,
    678901,
    2345678,
    90123456,
    789012345,
    6789012345,
    67890123456,
    789012345678
]

for i in testcases:
    print(i, EnglishInt(i))