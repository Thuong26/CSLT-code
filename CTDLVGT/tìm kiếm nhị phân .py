def timkiemnhiphan(a,x):
     left=0
     right=len(a)-1
     while left<=right:
          mid=(left+right)//2
          if a[mid]==x: return mid
          if a[mid]>x:
               right=mid-1
          else:
               left=mid+1
     return -1

a=[1,2,3,4,5,6,7,8,9,10]
t=timkiemnhiphan(a,int(input("Nhap so can tim: ")))
if t!=-1:
     print("So can tim nam o vi tri so "+str(t+1))
else:
     print("khong tim thay !")
