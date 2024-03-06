def LinearSearch(a,n,x):
    i=0
    while i<n and a[i] != x:
        i=i+1
    if i<n: return i
    else: return -1
a=[5,11,10,20,26,21,81,1]
n= len(a)
x=int(input("x="))
print(LinearSearch(a,n,x))
