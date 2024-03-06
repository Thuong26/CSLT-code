# cho n chuỗi ký tự, viết chương trình để in lên chuỗi dài nhất 
# và độ dài của nó. kiểm tra điều kiện n>0, nếu n<=0 thì trả về
# None.
# input:
# 3
# PHP 
# Exercises
# Backend
# output:
# Exercises
# 9
# input:
# 0
# output:
# None
n=int(input())
l=[]
if n<=0:
    print('None')
else:
    for i in range(n):
        s=input()
        l=l+[s]
    max=len(l[0])
    for i in l:
        if len(i)>max:
            max=len(i)
            x=i
    print(x)
    print(max)