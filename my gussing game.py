import random

gussestaken=0

guesstries=6

print('what is your name?')
myName=input()

print('whats the password?')
password = input()

if password == '12345':

    number=random.randint(1,80)
    print('hmm,'+myName+' i am thinking of a number between 1 and 80.')

    for i in range(6): 
        gussestaken = gussestaken + 1
            
        print('Take a guess.You have ' + str(guesstries) + ' tries.')
        guesstries = guesstries - 1
        guess=input()
        guess=int(guess)
        
        if guess < number:
            print('your guess is too low')
        if guess > number:
            print('your guess is too high')
        if guess == number:
            break
        
    if guess == number:
        gussestaken = str(gussestaken)
        print('good job ' + myName + ' you guessed my number in ' + gussestaken + ' guesses')
    if guess != number:
        number = str(number)
        print('nope ' + myName + ' i was thinking of ' + number)
        
        
        



        
        
        

