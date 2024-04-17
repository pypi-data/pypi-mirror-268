def sum(n):
    if n == 0 :
        return 0
    else:
        return n + sum(n-1)
n = int(input("Enter the Number:"))
res = sum(n)
print(f"The sum of First {n} Natural Numbers are :",res)
