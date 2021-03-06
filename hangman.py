import random
def get_list():
    return ['''
   +----+
        !
        !
        !
       ===
       ===''','''
    +----+
    0    !
         !
         !
       ===
       ===''','''
    +----+
    0    !
    !    !
         !
       ===
       ===''','''
    +----+
    0    !
   /!    !
         !
       ===
       ===''','''
    +----+
    0    !
   /!\   !
         !
       ===
       ===''','''
    +----+
    0    !
   /!\   !
   /     !
       ===
       ===''','''
    +----+
    0    !
   /!\   !
   / \   !
       ===
       ===''','''
    
    +----+
   (0)   !
   /!\   !
   / \   !
       ===
       ===''']
HANGMAN_PICS = get_list()
    
words = {'colors':'red orange yellow green blue white black brown indigo violate' .split(),
         'shapes':'circle square septagon triangle dodecadon ellipse rhombus trapezoid hexagon pentagon' .split(),
        'animals':'bat bear cow pig rhino wombat panda frog turtle whale zebra cat dog wolf lion lama fox eagle crab shark fish squid rat hamster mouse' .split(),
         'fruits':'banana starfruit orange pear tomato apple coconut pomagranete mango durian papaya grape stawberry' .split()}       

def getRandomWord(wordDict):
    wordkey = random.choice(list(wordDict.keys()))
    
    wordIndex = random.randint(0,len(wordDict[wordkey]) - 1)
    return [wordDict[wordkey][wordIndex], wordkey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:',end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print('you have aready guessed that letter. Choose another letter')
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
            print('PLEASE ENTER A LETTER')
        else:
            return guess

def playAgain():
    print('do you want to play again?(yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')

difficulty = ' '
while difficulty not in 'EMHI':
    print('Enter difficilty: E - easy, M - medium, H - hard, I - impossible.')
    difficulty = input().upper()
    
if difficulty == 'M':
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[6]

if difficulty == 'H':
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[6]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[4]
    
if difficulty == 'I':
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[6]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[4]
    del HANGMAN_PICS[3]
    del HANGMAN_PICS[2]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secretword is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters: 
            print('yeah you have won! The secret word was "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('you ran out of guesses\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses,the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            HANGMAN_PICS = get_list()
            difficulty = ' '
            while difficulty not in 'EMHI':
                print('Enter difficilty: E - easy, M - medium, H - hard, I - impossible.')
                difficulty = input().upper()
                
            if difficulty == 'M':
                del HANGMAN_PICS[7]
                del HANGMAN_PICS[6]

            if difficulty == 'H':
                del HANGMAN_PICS[7]
                del HANGMAN_PICS[6]
                del HANGMAN_PICS[5]
                del HANGMAN_PICS[4]
                
            if difficulty == 'I':
                del HANGMAN_PICS[7]
                del HANGMAN_PICS[6]
                del HANGMAN_PICS[5]
                del HANGMAN_PICS[4]
                del HANGMAN_PICS[3]
                del HANGMAN_PICS[2]
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
        
