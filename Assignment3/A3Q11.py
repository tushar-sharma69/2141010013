def findGCD(x,y):
   while y>0:
       r=x%y
       x=y
       y=r
   return x
   

def main():
    x=int(input('Enter 1st number: '))
    y=int(input('Enter 2nd number: '))
    gcd=findGCD(x,y)
    print('GCD=',gcd)
    
if __name__=='__main__':
    main()

