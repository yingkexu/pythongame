import random
import time
saves = 0
block = 0
dsaves = 0
dblock = 0
print('Please do not cheat and do more goes than you can.')
print('You are being attacked by a dragon.')
print('Do you want to have high hp and low attack(4)or low hp and high attack(5).')
player = int(input())

if player == 4:
    hp = 12
    attack = random.randint(2,3)
    hpp = 21
    att = 2
    
else:
    hp = random.randint(5,7)
    attack = 5
    hpp = 21
    att = 2

while hp > 0 and hpp > 0:
    goes = 2 + saves
    dragongoes = 2 + dsaves
    saves = 0
    block = 0
    dsaves = 0
    while goes > 0:
        print(' how much do you want to attack,(' + str(goes) + ')') 
        gow = int(input())
        choose = random.randint(6,7)

        if choose == 6:
            hpp = hpp - attack * gow + dblock * 2 
            goes = goes - gow
            if dblock > 0:
                dblock = dblock - 1

        if choose == 7:
            hpp = hpp + 1
            goes = goes - gow
            
        print('dragon ' + str(hpp))
        print('you ' + str(hp))
        time.sleep(1)
        
        if goes > 0:
            print('how much do you want to block, (' + str(goes) + ')')
            bb = input()
        else:
            print()
            bb = 0
        block = int(bb)
        gow2 = int(bb)
        goes = goes - gow2

        if goes > 0:
            print('How much reserves do you want, (' + str(goes) + ')')
            ss = input()
        else:
            ss = 0
            print()
        gow3 = int(ss)
        saves = int(ss)
        goes = goes - gow3
        
    dblock = 0
        
    while dragongoes > 0:
        dragongo = random.randint(8,11)

        if dragongo == 8:
            hp = hp - att + block * 2
            #print('The dragon attacked you!')
            if block > 0:
                block = block - 1

        if dragongo == 9:
            dgo2 = random.randint(1,3)
            if dgo2 == 1 or 2:
                #print('The dragon attacked you but missed!')
                hp = hp + 1
            if dgo2 == 3:
                #print('The dragon attacked you!')
                hp = hp - att + block * 2
                if block > 0:
                    block = block - 1
            

        if dragongo == 10:
            dsaves = dsaves + 1

        if dragongo == 11:
            dblock = dblock + 1
            

        print('dragon ' + str(hpp) + '(' + str(dragongoes) + ')')
        print('you ' + str(hp))
        dragongoes = dragongoes - 1
        time.sleep(3)

if hp > hpp:
    print('you win!')

else:
    print('you lose:( .')
    
    

            
            


