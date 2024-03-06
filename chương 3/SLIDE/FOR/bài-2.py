n=int(input())
kt=True
if n<2: print(n,'khong la SNT') 
elif n==2: print(n,'khong la SNT')
elif n%2==0:print(n,'khong la SNT')
else:
    for i in range(3,n,2):
        if n%i==0: kt=True
        else:  kt=False
    if kt==True: print(n,'la SNT')
    else: print(n,'khong la SNT')


# biến cờ/ biến trạng thái
# x=0
#n=int(input())
# for k in range (2,n)
#     if n%k==0:
#        x=1
#        break
# if x=1: print(n,'khong la SNT')   
# else: print(n,'la SNT') 
