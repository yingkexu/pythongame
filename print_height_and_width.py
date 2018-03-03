print('insert a height')
height = int(input())

print('insert a width')
width = int(input())

lines = '|'



for a in range(height):
    #print(lines)

    bottom = ''
    if a == 0 or a == height - 1:
        for i in range(width):
            bottom = bottom+'_'
        print(bottom)
    else:
        str = '|'
        for i in range(width - 2):
            str = str + ' '
        str = str + '|'
        
        print(str)

        
