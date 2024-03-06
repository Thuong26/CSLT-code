# cho một danh sách L gồm các số nguyên. Viết chương trình để 
# xác định các số lẻ lưu vào danh sách L1, các số chẵn lưu
# vào danh sách L2.
# input: 1 2 3 4 5 6 7 
# output: [1,3,5,7]
#         [2,4,6]
s=input().split()
l1=[]
l2=[]
for i in range(len(s)):
    if int(s[i])%2!=0:
        l1.append(int(s[i]))
    else:
        l2.append(int(s[i]))
print(l1)
print(l2)
