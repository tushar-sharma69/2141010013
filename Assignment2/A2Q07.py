import math
def areaTriangle(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def main():
    side1=float(input('Enter side1 of the triangle: '))
    side2=float(input('Enter side2 of the triangle: '))
    side3=float(input('Enter side3 of the triangle: '))
    assert side1+side2>side3 and side2+side3>side1 and \
    side1+side3>side2

    area=areaTriangle(side1,side2,side3)
    print('Area of the triangle is',area)

if __name__=='__main__':
    main()
