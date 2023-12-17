def checkPerfect(n):
   sum=0
   for i in range (1,n):
       if n%i==0:
           sum+=i
   if sum==n:
        return True
   else:
        return False

def main():
    n=int(input('enter an integer: '))
    res=checkPerfect(n)
    if res==True:
        print(n, 'is a perfect number')
    else:
        print(n, 'is not a perfect number')

if __name__=='__main__':
    main()
