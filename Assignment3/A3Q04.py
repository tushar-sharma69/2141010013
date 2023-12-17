import random
spin_result=random.randint(0,36)
print('Spin Result =',spin_result)
if spin_result==0:
    print('Pay 0')
elif spin_result==0:
    print('Pay 00')
else:
    if spin_result in [1,3,4,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        print('Pay Red')
    else:
        print('Pay Black')

if spin_result%2==0:
    print('Pay Even')
else:
    print('Pay Odd')

if 1<=spin_result<=18:
    print('1 to 18')
else:
    print('19 to 36')

