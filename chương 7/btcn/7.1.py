#  Viết chương trình:
#  -Cho phép nhập vào một chuỗi ký tự bất kỳ;
#  -Chương trình thực hiện đếm có bao nhiêu chữ cái in hoa, chữ cái in thường, chữ số và ký tự khác (bao gồm 
#  ký tự trắng) xuất hiện trong chuỗi trên;
#   -In kết quả lên màn hình.
#   TEST:
#   Input:Python Programming Class @2021!
#   Output:
#   In hoa: 3
#   In thuong: 19
#   Chu so: 4
#   Khac: 5
st=input()
def dem(st):
    h=0
    t=0
    s=0
    k=0
    for i in st:
        if i.isupper():h=h+1
        elif i.islower(): t=t+1
        elif i.isnumeric(): s=s+1
        else: k=k+1
    return h,t,s,k
def inkq():
    print('In hoa:',h)
    print('In thuong:',t)
    print("chu so:",s)
    print('Khac:',k)
h,t,s,k=dem(st)
inkq()

