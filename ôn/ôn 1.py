# Cho 3 chuỗi ký tự, viết chương trình đảo ngược các kí tự của chuỗi kí tự và in kết quả lên man hình 
# input:
# Python 
# list
# exercises
# output:
# nohtyp
# tsil
# sesicrexe
s=input()
s1=input()
s2=input()
l=""
l1=""
l2=""
for i in range(len(s)-1,-1,-1):
    l=l+s[i]
for i in range(len(s1)-1,-1,-1):
    l1=l1+s1[i]
for i in range(len(s2)-1,-1,-1):
    l2=l2+s2[i]
print(l)
print(l1)
print(l2)
