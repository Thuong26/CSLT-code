def tich(n):
    if n== 1:
        return 1
    return n * tich(n-1)
n=int(input("n="))
if n<=0 : n=int(input("n="))
print(tich(n))

# def tich(n):
#     P=1
#     for i in range(1,n+1):
#         P=P*i 
#     return P
# n=int(input("n="))
# if n<0: n=int(input("n="))
# print(tich(n))

