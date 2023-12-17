def discount(price):
    discount_amount = price * 0.60  # 60% discount
    new_price = price - discount_amount
    return discount_amount, new_price

def main():
    list1 = [4.95, 9.95, 14.95, 19.95, 24.95]

    print("Original price     Discounted amount        New price")

    for price in list1:
        discount_amount, new_price = discount(price)
        print("{:.2f}                   {:.2f}                   {:.2f}".format(price, discount_amount, new_price))

if __name__ == "__main__":
    main()
