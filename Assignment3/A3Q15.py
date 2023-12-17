def sumNum(n):
    res=0
    while(n>0):
        dig=n%10
        res=res+dig
        n=n//10
    return res
        
def main():
    n=int(input('Enter a number:'))
    result=sumNum(n)
    print( "Sum of digits of ",n," is ",result)

if __name__=='__main__':
    main()



