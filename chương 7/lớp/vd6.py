# Vídụ:Viết chương trình nhập vào tên và số lượng của 4 một
# mặt hàng bất kỳ, in lên màn hình bảng thực đơn theo mẫu sau.
# sandwiches........   4
# apples............  12
# cups..............   4
# cookies...........8000
ten=[]
soluong=[]
for i in range(4):
    T=input('mat hang: ')
    ten=ten+[T]
    SL=input('so luong: ')
    soluong=soluong+[SL]
for i in range (0,4):
    print(ten[i].ljust(15,'.'),end='')
    print(soluong[i].rjust(5))