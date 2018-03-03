
print('input a number')
number = input()

for i in range(int(number)):
    o = ''
    for j in range(i + 1):
        o = o + ' *'
    print(o)
    
