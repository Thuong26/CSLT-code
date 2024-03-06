import math
n = int(input())
if n <= 2 or n >= 1000:
   print("Vui long nhap lai!")
else:
   for i in range(2, n + 1):
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                #Thoat vong lap
                break
        #Neu khong thoat vong lap thi khoi lenh else se duoc thuc hien
        else:
            print(i, end=' ')