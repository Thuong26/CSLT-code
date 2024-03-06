# Viết chương trình:
# -Nhập vào một chuỗigồmcác từ được phân tách bởi dấu phẩy;
# -Chương trìnhthực hiệnloại bỏ các từ trùng lắp,sau đó sắp xếp các từ theo thứ tự bảng chữ cái, phân 
# tách nhau bởi dấu phẩy rồi in kết quả ra màn hình.
# TEST:
# Input: without,hello,bag,world,bag,hello
# Output: bag,hello,without,world
s=input()
L=[]
L=s.split(',')
def xoa(L):
    K=[]
    for i in range(len(L)):
        if L[i] not in K:
            K.append(L[i])
    return K
def inkq(K):
    K.sort()
    K=','.join(K)
    print(K)
K=xoa(L)
inkq(K)
