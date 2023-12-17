def series(x,n):
    error=0.00001
    sum=1
    term=1
    i=0

    while abs(term)>error:
        i+=1
        term=term*x/i
        sum+=term

    return sum
        
def main():
    x=float(input('Enter the value of x:'))
    n=float(input('Enter number of terms:'))
    result=series(x,n)
    print('Result=',result)

if __name__=='__main__':
    main()


