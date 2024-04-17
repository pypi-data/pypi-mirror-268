def power(b,e):
    if e == 0:
        return 1
    else:
        return b*pow(b,e-1)
b = int(input("Enter the base value:"))
e = int(input("Enter the exponent value:"))
res = pow(b,e)
print(f"The power of {b} ^ {e} is :",res)
