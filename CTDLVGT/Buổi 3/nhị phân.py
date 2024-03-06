s=[]
n=int(input("n="))
m=int(input("m="))
for i in range(n):
    s.append(0)
def inchuoi(s,i,n):
    for j in range(0,m):
        s[i]=j
        if i==n-1: print(s)
        else: inchuoi(s,i+1,n)
inchuoi(s,0,n)

# s=b=[]
# n=int(input("n="))
# k=int(input("k="))
# for i in range(n):
#     s.append(0)
#     b.append(True)
# def xuli(s,b,n,k,i):
#     for j in range(n):
#         if b[j]:
#             s[i]=j
#             b[j]=False
#             if i==k-1: print(s)
#             else: xuli(s,b,n,k+1,i)
#             b[j]=True
# xuli(s,b,n,k,0)