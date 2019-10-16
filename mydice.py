import random

print('This is a dice roller')

x='y'

while x == 'y':

    z = random.randint(1,6)

    if z==1:
        print('----------')
        print('|         |')
        print('|    0    |')
        print('|         |')
        print('----------')
    if z==2:
            print('----------')
            print('|         |')
            print('|  0  0   |')
            print('|         |')
            print('----------')
    if z==3:
            print('----------')
            print('|    0    |')
            print('|    0    |')
            print('|    0    |')
            print('----------')
    if z==4:
            print('----------')
            print('|  0    0 |')
            print('|         |')
            print('| 0     0 |')
            print('----------')
    if z==5:
            print('----------')
            print('| 0     0 |')
            print('|    0    |')
            print('| 0     0 |')
            print('----------') 
    if z==6:
            print('----------')
            print('| 0     0 |')
            print('| 0     0 |')
            print('| 0     0 |')
            print('----------')
    x = input('Press y to roll again ')
