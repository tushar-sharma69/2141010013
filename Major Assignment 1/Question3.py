def convert_to_decimal(number, base):
    decimal_value = 0
    power = 0

    for digit in reversed(number):
        decimal_value += int(digit, base) * (base ** power)
        power += 1

    return decimal_value

def convert_from_decimal(decimal_value, new_base):
    result = ""
    
    while decimal_value > 0:
        remainder = decimal_value % new_base
        result = str(remainder) + result
        decimal_value //= new_base

    return result if result else "0"

def main():
        input_number = input("Enter the number to convert: ").upper()
        input_base = int(input("Enter the base of the input number (2-16): "))
        output_base = int(input("Enter the base for the result number (2-16): "))

        if not (2 <= input_base <= 16) or not (2 <= output_base <= 16):
            print("Error: Bases must be between 2 and 16.")
            return

        decimal_value = convert_to_decimal(input_number, input_base)

        result_number = convert_from_decimal(decimal_value, output_base)

        print(f"The result in base {output_base} is: {result_number}")
if __name__ == "__main__":
    main()
