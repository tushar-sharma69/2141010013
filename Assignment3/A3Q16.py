def armstrong(i):
    num = i
    orig = num
    sum = 0
    while num > 0:
        dig = num % 10
        sum = sum + dig ** 3
        num //= 10
    if orig == sum:
        print(orig)

def main():
    i = 1
    while i <= 1000:
        armstrong(i)
        i = i+1

if __name__=='__main__':
    main()
