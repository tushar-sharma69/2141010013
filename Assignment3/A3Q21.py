def prime_factors(n):
    i = 2
    while i <= n:
        if n % i == 0:
            print(i)
            n //= i
        else:
            i += 1

def main():
    n = 0
    while n < 2:
        n = int(input("Enter an integer: "))
        if n < 2:
            print("Please enter an integer greater than or equal to 2.")

    print("The prime factors of",n," are:")
    prime_factors(n)

if __name__ == "__main__":
    main()
