# Viết chương trình để loại bỏ các phần tử trong một danh sách tại vị 
# trí có index: 1,3 và 4 cho trước.
# input: nhập vào một dãy các từ, mỗi từ cách nhau đúng 1 ký tự trắng:
# output: in lên màn hình một danh sách mới đã được xóa đi các từ ở 
# vị trí index cho trêN
# test:
#      Red Green White Black Pink Yellow
#      ['Red','While','Yellow']
# test2: 
#     An Binh Nam
#     ['An','Nam']
# test3:
#     An
#     ['An']
s=input().split()
l=[]
m=[]
for i in range(len(s)):
    if i==1:
       l.append(s[i])
    if i==3:
        l.append(s[i])
    if i==4:
        l.append(s[i])
for i in range(len(s)):
    if s[i] not in l:
        m.append(s[i])
print(m)
