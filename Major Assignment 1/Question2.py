def hex2int(hex_digit):
    hex_digit = hex_digit.upper()  
    
    if hex_digit not in '0123456789ABCDEF':
        print("Error: Invalid hexadecimal digit.")
        exit()

    decimal_value = int(hex_digit, 16)
    return decimal_value

def int2hex(decimal_value):
    if not (0 <= decimal_value <= 15):
        print("Error: Value outside the expected range (0-15).")
        exit()

    hex_digit = hex(decimal_value)[2:].upper()  
    return hex_digit

hex_input = input("Enter a hexadecimal digit: ")
decimal_result = hex2int(hex_input)
print(f"The equivalent decimal value is: {decimal_result}")

decimal_input = int(input("Enter an integer between 0 and 15: "))
hex_result = int2hex(decimal_input)
print(f"The equivalent hexadecimal digit is: {hex_result}")
