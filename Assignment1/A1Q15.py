x=int(input('Enter 1st integer: '))
y=int(input('Enter 2nd integer: '))
z=int(input('Enter 3rd integer: '))
maximum = max(x,y,z)
minimum = min(x,y,z)
middle=(x+y+z)-maximum-minimum
print(minimum,middle,maximum)
