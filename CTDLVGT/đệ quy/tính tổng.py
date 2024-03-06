def tong(n):
    if n== 1:
        return 1
    return n + tong(n-1)
n=int(input("n="))
if n<=0 : n=int(input("n="))
print(tong(n))

# def tinh_tong(n):
#     tong=0
#     for i in range(1,n+1):
#         tong=tong+i
#     return tong
# n=int(input("n="))
# if n<0 : n=int(input("n="))
# print(tinh_tong(n))

# n = int(input('Nhap n = '))
# tong = n*(n+1)/2
# print('Tong S = 1 + 2 + ... + n la:', tong)
