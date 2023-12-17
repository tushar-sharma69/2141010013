n=int(input('Enter a four digit number:'))
r1=n//1000  
r2=(n//100)%10
r3=(n//10)%10
r4=n%10
sum=r1*(1-r1%2)+r2*(1-r2%2)+r3*(1-r3%2)+r4*(1-r4%2)
print('Sum of even digits of',n,'=',sum)
