import time
import os
os.system('cls')
print('                 happy birthday daddy!')

#The following code is not needed

p1 = """           0
          /!\
          / \

          """

p2 = """          0    \o
          /!\    !-
          / \   / \

          """

p3 = """          Happy Birthday!      

           0    \o
          /!\    !-
          / \   / \

          """

p4 = """

               Happy Birthday!      

           0    o
          -!-  -!-
          / \  / \

          """

p5 = """

               Happy Birthday!      

          \0/   o
           !   -!-
          / \  / \

          """

p6 = """

               Happy Birthday!      

          \0/   o     0
           !   -!-   /!\
          / \  / \   / \

          """

p7 = """
               Happy Birthday!      

          \0/   o     0     o
           !   /|\   /!\  -!-
          / \  / \   / \   / \

          """


p8 = """           daddy   yingke   mummy   yingying
             ^        ^       ^        ^
             ^        ^       ^        ^ 
            \0/      \o/     \0/      \o/
             !        |       !        !    
            / \      / \     / \      / \

            """

def print_file(filename, sleep_time):
    os.system('cls')
    with open(filename) as f: 
        print(f.read())
    time.sleep(sleep_time)

time.sleep(8)

print_file('p1.txt', 2)

print_file('p2.txt', 2)

print_file('p3.txt', 2)

print_file('p4.txt', 2)

print_file('p5.txt', 2)

print_file('p6.txt', 2)

print_file('p7.txt', 2)

print_file('p8.txt', 10)


#The following code is wrong

#print('')
#print(p2)
#time.sleep(1)
#print(p3)
#time.sleep(1)
#print(p4)
#time.sleep(1)
#print(p5)
#time.sleep(1)
#print(p6)
#time.sleep(1)
#print(p7)
#time.sleep(1)
#print(p8)
#time.sleep(10)


