def tow(n,s,a,t):
    if n == 1:
        print(f"Move disk 1 from {s} to {t}")
        return
    tow(n-1,s,a,t)
    print(f"Move disk {n} from {s} to {t}")
    tow(n-1,a,s,t)
n = int(input("Enter the number of Disk:"))
tow(n,'A','B','C')
