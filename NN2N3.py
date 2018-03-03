def add0(a, b):
    return a + b
        
def times0(a,b):
    return a * b

def divide0(a,b):
    return a / b

print('input n')
n = int(input())
print('input n2')
n2 = int(input())
print('input n3')
n3 = int(input())
print('input n4')
n4 = int(input())
asonsum = add0(n,n2)
ssum = times0(n3,asonsum)
print(divide0(ssum,n4))
