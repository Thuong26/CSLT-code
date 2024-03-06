from ast import Delete

class Student:
    def __init__(self,id,name,classs,mark1,mark2,ave,grade):
        self.id=id
        self.name= hoten
        self.classs= lop
        self.mark1= ma1
        self.mark2= ma2
        self.ave=0
Listsv=[]
#Cau 1: Them sinh vien
def addSV():
    infor={ 'id' : '',
            'name' : '',
            'class' : '',
            'mark1' : '',
            'mark2' : '',
        }
    id=input("Nhap ma ID cua sinh vien:")
    while True:
        k=0
        for i in range(len(Listsv)):
            if Listsv[i]['id']!=id:
                k=k+1
        if len(Listsv)==0:
            break
        elif k==len(Listsv):
            break
        else:
            print("Ma ID da ton tai")
            id=input("Nhap ma ID cua sinh vien:") 
    infor['id']=id
    name=input("Nhap ho ten:")
    infor['name']=name
    classs=input("Nhap lop:")
    infor['class']=classs
    mark1=float(input("Nhap mark1:"))
    infor['mark1']=mark1
    mark2=float(input("Nhap mark2:"))
    infor['mark2']=mark2
    Listsv.append(infor)
    print("Them vao thanh cong")
#Cau 2: Xoa sinh vien
def delsv():
    id=input("Nhap ma ID cua sinh vien can xoa:")
    i=0
    k=0
    while True:
        i=0
        while i<len(Listsv):
            if Listsv[i]['id']==id:
                Listsv.remove(Listsv[i])
                k=1
                break
            i=i+1
        if k==1:
            break 
        else:
            print("khong tim thay id")
            id=input("Nhap ma ID cua sinh vien can xoa:")  
#cau 3: sua chua thong tin
def editsv():
    id=input("Nhap ma ID cua sinh vien can sua chua thong tin:")
    k=0
    while True:
        for i in range(len(Listsv)):
            if Listsv[i]['id']==id:
                name=input("Nhap ho ten:")
                Listsv[i]['name']=name
                classs=input("Nhap lop:")
                Listsv[i]['class']=classs
                mark1=float(input("Nhap mark1:"))
                Listsv[i]['mark1']=mark1
                mark2=float(input("Nhap mark2:"))
                Listsv[i]['mark2']=mark2
                k=1
        if k==0:
            print("khong tim thay id")
            id=input("Nhap ma ID cua sinh vien can sua chua thong tin:")      
        elif k==1:
            break
#Cau 4: in
def printsv():
    for i in range(len(Listsv)):
        print(Listsv[i])
#Cau 5: tinh diem trung binh
def avesv():
    for i in range (len(Listsv)):
        a=Listsv[i]['mark1']
        b=Listsv[i]['mark2']
        ave=(a+b)/2
        print('ID:',Listsv[i]['id'],'HoTen:',Listsv[i]['name'],'co diem trung binh cong la:',round(ave,2))

#Cau 6: Tính điểm trung bình cho môn 1 của toàn bộ sinh viên: averageMark1
def avm1():
    dem=0
    tong=0
    for i in range (len(Listsv)):
        dem=dem+1
        tong=tong+Listsv[i]['mark1']
    print('mark 1 co diem trung binh cong la:',round(tong/dem,2))
#Cau 7: Tính điểm trung bình cho môn 2 của toàn bộ sinh viên : averageMark2
def avm2():
    dem=0
    tong=0
    for i in range (len(Listsv)):
        dem=dem+1
        tong=tong+Listsv[i]['mark2']
    print('mark 2 co diem trung binh cong la:',round(tong/dem,2))
#Cau 8: Tìm xem sinh viên nào có điểm trung bình học tập thấp nhất, in ra toàn bộ thông tin của SV đó
def avemin():
    min=11
    for i in range (len(Listsv)):
        a=Listsv[i]['mark1']
        b=Listsv[i]['mark2']
        ave=(a+b)/2
        if min>ave:
            min=ave
            k=i
    print('ID:',Listsv[k]['id'],', HoTen:',Listsv[k]['name'],', Lop:',Listsv[k]['class'],', Mark 1:',Listsv[k]['mark1'],', Mark 2:',Listsv[k]['mark2'],', co diem trung binh cong tham nhat=',round(min,2))
#Cau 9: Tìm xem sinh viên nào có điểm trung bình học tập cao nhất, in ra toàn bộ thông tin của SV đó 
def avemax():
    max=0
    for i in range (len(Listsv)):
        a=Listsv[i]['mark1']
        b=Listsv[i]['mark2']
        ave=(a+b)/2
        if max<ave:
            max=ave
            k=i
    print('ID:',Listsv[k]['id'],', HoTen:',Listsv[k]['name'],', Lop:',Listsv[k]['class'],', Mark 1:',Listsv[k]['mark1'],', Mark 2:',Listsv[k]['mark2'],', co diem trung binh cong cao nhat=',round(max,2))
t=1
print('0: Thoat chuong trinh \n1: Thêm sinh viên \n2: Xóa sinh viên \n3: Sửa sinh viên4: Xem danh sách sinh viên \n5: Tính điểm trung bình học tập cho từng sinh viên (average= (mark1+mark2)/2 \n6: Tính điểm trung bình cho môn 1 của toàn bộ sinh viên: averageMark1 \n7: Tính điểm trung bình cho môn 2 của toàn bộ sinh viên : averageMark2 \n8: Tìm xem sinh viên nào có điểm trung bình học tập thấp nhất, in ra toàn bộ thông tin của SV đó \n9: Tìm xem sinh viên nào có điểm trung bình học tập cao nhất, in ra toàn bộ thông tin của SV đó ')
while t!=0:
    t=int(input("Nhap:"))
    if t==1:
        addSV()
    elif t==2:
        delsv()
    elif t==3:
        editsv()
    elif t==4:
        printsv()
    elif t==5:
        avesv()
    elif t==6:
        avm1()
    elif t==7:
        avm2()
    elif t==8:
        avemin()
    elif t==9:
        avemax()
    
