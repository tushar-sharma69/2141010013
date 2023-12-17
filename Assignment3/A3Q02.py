import sys
human_years=float(input('Enter the no of human years: '))

if human_years<0:
    print('Error: Please enter a non negative no of human years')
    sys.exit(0)
elif human_years<=2:
    dog_years=human_years*10.5
else:
    dog_years=2*10.5+(human_years-2)*4

print(human_years,'no of human years is equivalent to ',dog_years,'dog years')
