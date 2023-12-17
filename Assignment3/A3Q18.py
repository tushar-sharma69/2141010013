def multiply(x,y):
    res=0
    while(y>0):
        res=res+x
        y=y-1
    return res  
    
def main():
    x=int(input('Enter the first number :'))
    y=int(input('Enter the second number :'))
    result=multiply(x,y)
    print("The product of",x,"and",y,"is",result)

if __name__=='__main__':
    main()



