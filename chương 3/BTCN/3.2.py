a=int(input('M1='))
b=int(input('M2='))
c=int(input('M3='))
tt=int(input('S='))
if 0<tt<=100:
    T=a*tt
if 101<=tt<=150:
    T=a*100+b*(tt-100)
if tt>=151:
    T=a*100+b*50+c*(tt-150)
print('Phai tra='+str(T))