import random

possibleNumbers = []
l = range(10)

# get all possible numbers
for i in l:
    n1 = str(i)
    l2 = list(l)
    l2.remove(i)
    for j in l2:
        n2 = str(j)
        l3 = list(l2) 
        l3.remove(j)
        for k in l3:
            n3 = str(k)
            possibleNumbers.append(n1 + n2 + n3)
            
random.shuffle(possibleNumbers)

step = 0
guessingNumber = possibleNumbers[0]
print('**********************************************************************************')
print('step ' + str(step))
print(guessingNumber)
print('**********************************************************************************')
possibleNumbers.remove(guessingNumber)

# store previous guessing number
previousGussingNumber = ''
previousS = ''

def remove(numbers):
    for n in numbers:
        possibleNumbers[:] = [x for x in possibleNumbers if not n in x]
        
def removeNumberInPosition(number, position):
    possibleNumbers[:] = [x for x in possibleNumbers if not x[position] == number]
    
def removeNumberNotContainAtLeastMatchDigits(number, numberOfMatchDigit):
    possibleNumbers[:] = [x for x in possibleNumbers if countMatchDigits(x, number, numberOfMatchDigit)]
    
def countMatchDigits(possibleNumber, number, numberOfMatchDigit):
    count = 0
    for p in possibleNumber:
        for n in number:
            if p == n:
                count += 1
    if count >= numberOfMatchDigit:
        return True
    return False

def keepNumber(number):
    for n in number:
        possibleNumbers[:] = [x for x in possibleNumbers if n in x]

while True:
    s = raw_input('what it returned?')
    
    # b. remove numbers that contains digit in s
    if s == 'b':
        remove(guessingNumber)
    else:  
                    
        # only p. remove numbers that has same number in same position
        if 'f' not in s:
            for i, n in enumerate(guessingNumber):
                removeNumberInPosition(n, i)
                
        # at least contains len(s) digits in guessing number. eg 'pp', possible numbers should at least have 2 of the guessing number
        removeNumberNotContainAtLeastMatchDigits(guessingNumber, len(s))
            
        # if len(s) < previous len(s), remove new numbers. changed number is what we want
        if len(s) < len(previousS):
            for p in previousGussingNumber:
                if p not in guessingNumber:
                    keepNumber(n)
            for g in guessingNumber:
                if g not in previousGussingNumber:
                    remove(g)
                    
            
        
    # store previous guessing number and s
    previousGussingNumber = guessingNumber
    previousS = s    
            
    step += 1
    guessingNumber = possibleNumbers[0]
    print('**********************************************************************************')
    print('step ' + str(step))
    print(guessingNumber)
    print('**********************************************************************************')
    print('possible numbers: ' + str(len(possibleNumbers)))
    print(possibleNumbers)
    possibleNumbers.remove(guessingNumber)
    
    