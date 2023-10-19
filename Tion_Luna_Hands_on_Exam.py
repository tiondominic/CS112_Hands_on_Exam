numbertoConvert = eval(input("Number to convert: "))
conversion = eval(input("Would you like to convert " + str(numbertoConvert) + " to 1(binary), 2(octal), 3(hexadecimal): "))

if conversion == 1:
    print(format(numbertoConvert, "b"))
elif conversion == 2:
    print(format(numbertoConvert, "o"))
elif conversion == 3:
    print(format(numbertoConvert, "x"))
else:
    print("invalid input")


