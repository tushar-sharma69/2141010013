def series(x,n):
    sum=1
    term=1
    i=0
    count=1
    while count<n:
        i=i+2
        term=-term*(x*x)/(i*(i-1))
        sum+=term
        count+=1

    return sum
        
def main():
    x=float(input('Enter the value of x:'))
    n=float(input('Enter number of terms:'))

    result=series(x,n)
    print('Result=',result)

if __name__=='__main__':
    main()
