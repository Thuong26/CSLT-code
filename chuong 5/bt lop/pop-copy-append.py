L=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# tach nhung so nguyen tai vi tri co so chi muc chan trong L va luu vao M
# b xoa nhung phan tu taij vi tri co so chi muc chan trong L. in list len man hinh
#a)
M=[]
for i in range(0,len(L)-1):
    if i%2==0:
        M.append(L[i])
# b)
K=[]
for i in range(len(L)):
    if i%2!=0:
        K.append(L[i])
L=K.copy()
print(L)