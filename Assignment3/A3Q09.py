def max3(x,y,z):
    def max2(x,y):
        if x>y:
            return x
        else:
            return y
    max_of_two=max2(x,y)
    max_of_three=max2(max_of_two,z)
    return max_of_three
   

def main():
    x=float(input('Enter 1st number: '))
    y=float(input('Enter 2nd number: '))
    z=float(input('Enter 3rd number: '))

    result=max3(x,y,z)
    print('Maximum among three integers=',result)
    
if __name__=='__main__':
    main()
