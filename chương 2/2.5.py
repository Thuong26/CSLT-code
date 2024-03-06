from cmath import sqrt
import math
sotienbd=int(input('So tien ban dau: '))
sothang=int(input('So thang gui: '))
T=float(input('Lai suat/thang: '))
m=sotienbd*(1+sothang*T)
print('Voi so tien ban dau '+str(sotienbd)+', sau',sothang,'thang gui, lai suat '+str(T)+'/thang \nThi so tien nhan duoc cuoi ky la:',m)