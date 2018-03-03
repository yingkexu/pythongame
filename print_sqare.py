print('write a number')
number = input()

for i in range (int(number)):
    strap = ''
    for j in range(int(number)):
        strap = strap + '* '
    print(strap)
    
    
