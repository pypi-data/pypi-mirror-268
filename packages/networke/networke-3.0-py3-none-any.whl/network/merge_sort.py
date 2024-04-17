def merge(a,depth = 0):
    if len(a) > 1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        merge(left,depth+1)
        merge(right,depth+1)
        print(" " * depth,'Dividing',a)
        print(" " * depth,"Merging",left,"and",right)
        a.clear()
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a.append(left[i])
                i += 1
            else:
                a.append(right[j])
                j += 1
        while i < len(left):
                a.append(left[i])
                i += 1
        while j < len(right):
                a.append(right[j])
                j += 1
        print(" " *depth,"Result:",a)
a = []
n = int(input("Enter the Upper Limit:"))
for i in range(n):
    ele = int(input("Enter the Elements:"))
    a.append(ele)
print("Before Sorting:",a)
merge(a)
print("Sorted Array:",a)
                
