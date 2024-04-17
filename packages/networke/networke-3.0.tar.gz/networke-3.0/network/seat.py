def find(total,vip,un):
    eli = []
    start = vip+1
    for seat in range(start,total-un + 1):
        if (seat - start+1)%7 == 0:
            eli.append(seat)
    return eli

total = int(input("Enter the total number of seats available in stadium:"))
vip = 200
un = 400

res = find(total,vip,un)
print("The eligible seats are :")
print(res)
print("The total number of eligible seat are:",len(res))
