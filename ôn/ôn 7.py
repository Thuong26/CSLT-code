# Viết chương trình để tìm các giá trị kiểu số lớn nhất và nhỏ nhất trong một 
# trong một danh sách không đồng nhất đã cho.
# input: 4 Python 3 2 version 5
# output: [5,2]
s=input().split()
L=[]
for i in range(len(s)):
    if s[i].isnumeric()==True:
        L.append(s[i])
L.sort()
K=[]
K.append(int(L[-1]))
K.append(int(L[0]))
# max=L[0]
# min=L[0]
# for i in range(len(L)):
#     if max< L[i]:
#             max=L[i]
#     if min> L[i]:
#             min=L[i]
# K=[]
# K.append(int(max))
# K.append(int(min))
print(K)
   
