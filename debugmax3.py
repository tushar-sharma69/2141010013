def max3(x,y,z):
    maxNUmber=0
        if x>y:
            if x>z:
                maxNumber=x
        elif y>z:
            maxNumber=y
        else:
            maxNumber=z
        return maxNumber

def main():
    x=int(input('Enter 1st number: '))
    y=int(input('Enter 2nd number: '))
    z=int(input('Enter 3rd number: '))
    maximum=max4(x,y,z)
    print('Maximum +',maximum)
    
if __name__=='__main__':
    main()
    
