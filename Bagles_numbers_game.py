import random

NUM_DIGITS = 3
print('Do you want hard(8 guesses) normal(10 guesses) or easy(12 guesses) or mabye you want impossible (6 guesses) ?')
level = input().lower()
diffic = level

if diffic == 'hard':
    MAX_GUESS = 8
elif diffic == 'normal':
    MAX_GUESS = 10
elif diffic == 'easy':
    MAX_GUESS = 12
else:
    MAX_GUESS = 6

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):    
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = [ ]
    for i in range (len (guess)):
        if guess [i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    if num == ' ':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'. split():
            return False

        return True

print('I am thinking of a %s digit number.   Try and guess what it is' %
    (NUM_DIGITS))
print('The clues I give are...')
print('when I say:    That means')
print('    Bagels        None of the digits is correct.')
print('    Pico        One digit is correct but in the wrong position.')
print('    Fermi        One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought of a number. You have %s guesses to get it.' %
          (MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            guess = input()

        print(getClues(guess, secretNum) + '  (you have done ' + str(guessesTaken) + ' guesses.)')
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' %
                  (secretNum))
            print('Do you want to play again? (yes or no)')
            if not input().lower().startswith('y'):
                break



