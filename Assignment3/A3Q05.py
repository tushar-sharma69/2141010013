decibels = float(input("Enter the number of decibels: "))
	
if decibels > 0 and decibels < 40:
    print('quieter than a quiet room.')
		
elif decibels == 40:
    print('about the same as a quiet room.')
	
elif decibels > 40 and decibels < 70:
    print('quieter than an alarm clock.')
elif decibels == 70:
    print('about the same as an alarm clock.')
		
elif decibels > 70 and decibels < 106:
    print('quieter than a lawn mower.')
	
elif decibels == 106:
    ('about the same as a lawn mower.')
	
elif decibels > 106 and decibels < 130:
    print(" quieter than a jackhammer.")
		
elif decibels == 130:
    print('about the same as a jackhammer.')
		
elif decibels > 130:
    print('way too loud.')
		
else:
    print('Please enter a correct data value.')
		
    print('Your sound level is')
