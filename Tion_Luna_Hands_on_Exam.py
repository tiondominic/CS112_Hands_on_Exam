numbertoConvert = eval(input("Number to convert: "))
conversion = eval(input("Would you like to convert " + str(numbertoConvert) + " to 1(binary), 2(octal), 3(hexadecimal): "))

if conversion == 1:
    print(bin(numbertoConvert).replace("0b", ""))
elif conversion == 2:
    print(oct(numbertoConvert).replace("0o", ""))
elif conversion == 3:
    print(hex(numbertoConvert))
else:
    print("invalid input")

