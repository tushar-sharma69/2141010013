def binary_to_decimal(binary_str):
    decimal_num = 0
    binary_str = binary_str[::-1]  

    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            decimal_num += 2 ** i

    return decimal_num

binary_input = input("Enter a binary number: ")

if all(bit in '01' for bit in binary_input):
    decimal_result = binary_to_decimal(binary_input)
    print(f"The equivalent decimal number is: {decimal_result}")
else:
    print("Invalid binary input. Please enter a valid binary number.")
