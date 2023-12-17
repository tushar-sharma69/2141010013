import sys
if len(sys.argv)==3:
	num1=int(sys.argv[1])
	num2=int(sys.argv[2])
	sum=num1+num2
	print('Sum=',sum)
else:
	print('Unexpected number of arguments')
