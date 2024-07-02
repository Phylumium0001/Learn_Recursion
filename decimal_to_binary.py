def binary_to_decimal(decimal):
    # Base Case - When the quotient is 0
    if (decimal == 0):
        return "0"
    else:
        return binary_to_decimal(decimal // 2) + str(decimal % 2)

print(binary_to_decimal(133))