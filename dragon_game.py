import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you, there are two caves. In one cave, theres a nice dragon who will share his treasure but in the other one theres a mean dragon who will eat you up!''')
    print()

def chooseCave():
    cave = ''
    while cave !='1' and cave !='2':
        print('which cave will you go into?(1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('you approach the cave...')
    time.sleep(1)
    print('Its dark and spooky...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('you hear a noise...')
    time.sleep(1)
    print('A massive dragon leaps at you it opens his jaws around your neck. Everynthing gose black...')
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    dragon = ''
    
    if chosenCave == str(friendlyCave):
        print('You wake up, you have met a friendly dragon, it shares its gold!')
        dragon = 'friendly'
    else:
        print('You met a mean dragon, whos going to eat you!')
        dragon =  'mean'
    return dragon

def fightDragon(dragon):
    hpHuman = 5
    hpDragon = 8
    if dragon == 'mean':
        action = ''
        while action != 'fight' and action != 'run':
            print('Do you want fight or run?(input fight or run)')   
            action = input()
            
        if action == 'fight':           
            print('do you want to use a bow or sword?(bow has less damage but two tries, sword has more damage but one try)')
            bos = input()
            
            while hpHuman > 0 and hpDragon > 0:
                 
                if bos == 'sword':
                    chop = random.randint(1,5)
                    ping = 0
                    ping2 = 0
                else:
                    chop = 0
                    ping = random.randint(1,5)
                    ping2 = random.randint(1,10)
                if chop == 1: 
                    print('chop oh no you missed')
                if ping == 1 or ping2 == 1 or ping2 == 2 or ping2 == 3:
                    print('ping you hit the dragon!')
                    hpDragon = hpDragon - random.randint(1,2)

                if chop == 1:
                    print(' chop you hit the dragon!')
                    hpDragon = hpDragon - random.randint(2,3)
        
                if chop == 2 or chop == 3 or ping == 2 or ping == 3:
                    print('whoosh you doged the dragon!')
                else:
                    print('bang you got hit by the dragon!')
                    hpHuman = hpHuman - 1

                print(str(hpDragon) + ' the dragons hp')
                print(str(hpHuman) + ' your hp')
                time.sleep(1)

            if hpHuman < hpDragon:
                print('you died!')
            else:
                print('you killed the dragon!')

        if action == 'run':
            print('you can go if you guess my number')

     
            guesstries=6
            gussestaken=0

            number = random.randint(1,100)
            print('hmm, i am thinking of a number between 1 and 100.')
       

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
                print('fine you can go because you guesesed my number in ' + gussestaken + ' guesses')
            if guess != number:
                number = str(number)
                print('nope  i was thinking of ' + number)

playAgain = 'yes'    
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    cave = chooseCave()
    dragon = checkCave(cave)
    
    fightDragon(dragon)
    print('Do you want to play again?(yes or no.)')
    playAgain = input()

        
