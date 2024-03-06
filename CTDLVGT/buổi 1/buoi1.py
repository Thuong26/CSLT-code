# a=int(input())
# b=int(input())
# print('a+b=',a+b)
# print('a-b=',a-b)
# print('a*b=',a*b)
# if b==0:
#     print('không có thương')
# else: 
#     print('a/b',a/b)

# bài2: giải phương trình bậc nhất

# a=int(input())
# b=int(input())
# if a==0:
#     print('phương trình vô nghiệm')
# else:
#     print('phuong trinh có nghiệm x=',-b/a)

# bài 3: giai phương trình bậc 2.

# from cmath import sqrt
# import math


# a=int(input())
# b=int(input())
# c=int(input())
# if a==0 :
#     if b==0:
#         print('phương trình vô số nghiệm')
#     else:
#         print('phuong trinh có nghiệm x=',-c/b)
# else: 
#     delta=b**2-4*a*c
#     if delta < 0:
#         print("Phương trình vô nghiệm")
#     elif delta == 0:
#         print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
#     else:
#         print("Phương trình có hai nghiệm phân biệt:")
#         print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
        # print("x1 = ", (-(b) - math.sqrt(delta))/(2*a) )
# bài 4: in ra tất cả các số nguyên tố từ 1 đến n:

# from pickle import TRUE


# n=int(input())
# for x in range(1,n+1):
#     prime = True
#     for i in range(2,x):
#         if (x%i==0):
#             prime = False
#     if prime == True:
#        print(x)
# bài 5: số hoàn hảo
# n=int(input())
# for t in range(1,n+1,1):
#     a=0
#     for i in range(1,t,1):
#         if t%i==0:
#             a=a+i
#     if a==t:
#         print(t)

# bai 6 tim phân tư lơn nhất của một dãy gồm n số nguyên

# n=int(input())
# l=[]
# for i in range(n):
#     a=int(input())
#     l=l+[a]
# max=l[1]
# for i in range(n):
#     if max<l[i]:
#         max=l[i]
# print('SLN của dãy là:'max)

# bài 7: tính n! với 0!=1, n!=n*(n-1)*(n-2)...!
# n=int(input('n='))
# if 0<=n<=100:
#     giaithua=1
#     for i in range(1,n+1): 
#         giaithua=giaithua*i
#     print(str(n)+'!='+str(giaithua))
# else: print()

# bài 8: Thực hiện phép cộng hai phân số 
# a=input().split('/')
# b=input().split('/')
# if int(a[0])!=0 and (b[1])!=0:
#         print((int(a[0])/int(a[1]))+(int(b[0])/int(b[1])))
# else:
#         print('khong hop le')

# #hãy in ra tất cả các số trong mảng A cùng với số lần xuất hiện của chúng
n=int(input())
l=[]
for i in range (n):
    a=int(input())
    l.append(a)
def sl(n,l):
    dem=0
    for i in l:
        if i==n:
            dem=dem+1
    return dem
def xoa(l):
    K=[]
    for i in range(len(l)):
        if l[i] not in K:
            K.append(l[i])
            B=sorted(K)
    return B
def inkq():
    print(xoa(l))
    for i in l:
        print(sl(i,l))
dem=sl(n,l)
B=xoa(l)
inkq()




