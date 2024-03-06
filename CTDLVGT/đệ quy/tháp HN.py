n = int(input('Nhap n = '))
def ThapHaNoi(n,Nguon, TrungGian, Dich):
    if n == 1:
        print('Dia n:',n,'di chuyen tu', Nguon,'den',Dich)
        return()
    ThapHaNoi(n-1, Nguon, Dich, TrungGian)
    print('Dia n:',n, 'di chuyen tu', Nguon, 'den', Dich)
    ThapHaNoi(n-1, TrungGian, Nguon, Dich)

ThapHaNoi(n,'Nguon','TrungGian','Dich')
