from cmath import sqrt
import math
canh1=int(input('Nhap 2 canh ke cua tam giac vuong \n'))
canh2=int(input(""))
canh3=math.sqrt(canh1**2+canh2**2)
print('Canh ke thu nhat la:',canh1,', canh ke thu hai:',canh2,', co canh huyen =',round(canh3,2),sep="")