def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        return True
    else:
        return False
        
def main():
    n=int(input('Enter a number to check if its palindrome:'))
    result=palindrome(n)
    print(result)

if __name__=='__main__':
    main()



