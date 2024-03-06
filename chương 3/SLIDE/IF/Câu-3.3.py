TT=float(input('Tieu thu='))
if 1<=TT<=100:
    Tien=550*TT
elif 101<=TT<=150:
    Tien=550*100+750*(TT-100)
elif 151<=TT<=200:
    Tien=550*100+750*50+950*(TT-150)
elif TT>=201: 
    Tien=550*100+750*50+950*50+1350*(TT-200)
VAT=Tien*0.1
tong=Tien+VAT
print('Phai tra='+str(tong))