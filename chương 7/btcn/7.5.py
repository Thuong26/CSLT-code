# Viết chương trình:
# -Nhập vào một chuỗigồmcác số nguyên, mỗi số cách nhau bởi một dấu cách;và một sốnguyênX;
# -Chương trình thực hiệntìm X trong dãy số trên, in lên màn hình thứ tự xuất hiện của X nếu có. 
# Nếu không tìm thấy thì trả về 0;
# TEST1:                                              EST2:
#     Input:1 30 44 12 15 24 93 100 24 52 15 34            Input:44 12 24 93 100 24 52
#           15                                                   15
#     Output:5                                             Output:0
#            11      
from re import L
s=input()
l=s.split()
x=int(input())
K=[]
for i in range(len(l)):
    m=int(l[i])
    K.append(m)
if x in K:
    for i in range(len(K)):
        if K[i]==x:
            print(i+1)
else: print('0')

# s=input().split(' ')
# x=int(input())
# l=[]
# for i in range(len(s)):
#     h=int(s[i])
#     if h==x:
#         l.append(i+1)
# if len(l)>0:
#     for j in l:
#         print(j)
# else:print(0)
# n=input()
# L=[]
# K=[]
# for i in range(0,len(n),1):
#     L=L+[n[i]]
# for t in range(0,len(L),1):
#     for i  in range(-1,-len(L),-1):
#         if L[i]==' ':
#             del(L[i])
#         if L[i]!=' ':
#             break
#     for i in range(0,len(L),1):
#         if L[0]==' ':
#             del(L[0])
#             break
#         if L[i]==' 'and L[i+1]==' ':
#             del(L[i])
#             break
# for i in range(0,len(L),1):
#     if i==0:
#         a=L[i].upper()
#     else:
#         a=L[i].lower()
#     K=K+[a]
# for t in range (0,len(K),1):
#     for i in range(0,len(K),1):
#         if K[i]==' ' and K[i+1]==',':
#             del(K[i])
#             break
#         elif K[i]==' ' and K[i+1]==';':
#             del(K[i])
#             break
#         elif K[i]==' ' and K[i+1]=='.':
#             del(K[i])
#             break
#         elif K[i]==' ' and K[i+1]==':':
#             del(K[i])
#             break
# A=''.join(K)
# print(A)