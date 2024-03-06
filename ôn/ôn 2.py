# cho một danh sách một từ, viết chương trình để chèn một phần tử 
# của danh sách
# input: nhập vào thứ 1 là một dãy các từ, mỗi từ cách nhau đúng 1
# kí tự trắng. Dòng thứ 2 là 1 từ
# output: in lên màn hình một danh sách mới gồm các phần tử từ 2 danh sách này
#  input:
#     Red Green Black
#     Blue
# # output:
#     ['Blue','Red','Blue','Green','Blue','Black']
l=[]
s=input().split()
tu=input()
l=l+[tu]
for i in s:
    l=l+[i]
    print(l)
    if i!=s[len(s)-1]:
        l=l+[tu]
print(l)