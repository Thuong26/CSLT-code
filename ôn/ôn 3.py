# Viết chương trình để tạo một danh sách mới gồm các phần tử chung từ 2 danh sách đã cho
# input: nhập vào hai dòng, mỗi dòng là một dãy các từ, mỗi từ cách nhau đúng 1 ký tự trắng
# output: in lên màn hình một danh sách mới gồm các phần tử chung của 2 danh sách trêN
# vd : input
#             Red Green White Orange
#             Green Black White Pink
#     output: Green White 
s=input().split()
s1=input().split()
l=[]
for i in range(len(s)):
    if s[i] in s1:
        l.append(s[i])
print(' '.join(l))
