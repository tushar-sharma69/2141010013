def coprime(x,y):
    if(x%y==0 or y%x==0):
        return False
    else:
        return True
        
def main():
    x=int(input('Enter the first number :'))
    y=int(input('Enter the second number :'))
    result=coprime(x,y)
    print(result)

if __name__=='__main__':
    main()



