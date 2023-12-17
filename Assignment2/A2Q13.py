def checkCollinearity(x1,y1,x2,y2,x3,y3):
    slope1=(y2-y1)/(x2-x1)
    slope2=(y3-y2)/(x3-x2)
    result= True if (slope1==slope2) else false
    return result

def main():
    x1=float(input('Enter the value of x1: '))
    y1=float(input('Enter the value of y1: '))
    x2=float(input('Enter the value of x2: '))
    y2=float(input('Enter the value of y2: '))
    x3=float(input('Enter the value of x3: '))
    y3=float(input('Enter the value of y3: '))

    result=checkCollinearity(x1,y1,x2,y2,x3,y3)
    print(result)
main()
