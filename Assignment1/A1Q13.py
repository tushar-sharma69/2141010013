import math
gravity=9.8
height=float(input('Enter the height:'))
vi=0
d=height
vf=math.sqrt(vi**2+2*gravity*d)
print('The final speed of the object =',vf)
