from ast import Delete
class SinhVien:
    def __init__(self,MaSV,name,classs,d1,d2):
        self.MaSV = MaSV
        self.name = name
        self.classs = classs
        self.diem1 = d1
        self.diem2 = d2
        self.TB = 0
DSSV=[]
def addSV():
    infor={ 'MaSV' : '',
            'name' : '',
            'class' : '',
            'diem1' : '',
            'diem2' : '',
        }
    MaSV=input("Nhap ma SV : ")
    while True:
        k=0
        for i in range(len(DSSV)):
            if DSSV[i]['MaSV']!=MaSV:
                k=k+1
        if len(DSSV)==0:
            break
        elif k==len(DSSV):
            break
        else:
            print("Ma ID da ton tai")
            MaSV=input("Nhap ma ID cua sinh vien:") 
    infor['MaSV']=MaSV
    name=input("Nhap ho ten:")
    infor['name']=name
    classs=input("Nhap lop:")
    infor['class']=classs
    d1=float(input("Nhap mark1:"))
    infor['diem1']=d1
    d2=float(input("Nhap mark2:"))
    infor['diem2']=d2
    DSSV.append(infor)
    print("Them vao thanh cong")
#Cau 2: Xoa sinh vien
def delsv():
    MaSV=input("Nhap ma ID cua sinh vien can xoa:")
    i=0
    k=0
    while True:
        i=0
        while i<len(DSSV):
            if DSSV[i]['MaSV']==MaSV:
                DSSV.remove(DSSV[i])
                k=1
                break
            i=i+1
        if k==1:
            break 
        else:
            print("khong tim thay id")
            MaSV=input("Nhap ma ID cua sinh vien can xoa:") 
#3 sua sinh vien
def editsv():
    MaSV=input("Nhap ma ID cua sinh vien can sua chua thong tin:")
    k=0
    while True:
        for i in range(len(DSSV)):
            if DSSV[i]['MaSV']==MaSV:
                name=input("Nhap ho ten:")
                DSSV[i]['name']=name
                classs=input("Nhap lop:")
                DSSV[i]['class']=classs
                d1=float(input("Nhap mark1:"))
                DSSV[i]['diem1']=d1
                d2=float(input("Nhap mark2:"))
                DSSV[i]['diem2']=d2
                k=1
        if k==0:
            print("khong tim thay id")
            MaSV=input("Nhap ma ID cua sinh vien can sua chua thong tin:")      
        elif k==1:
            break
#Cau 4: in
def printsv():
    for i in range(len(DSSV)):
        print(DSSV[i])
#Cau 5: tinh diem trung binh
def avesv():
    for i in range (len(DSSV)):
        a=DSSV[i]['diem1']
        b=DSSV[i]['diem2']
        TB=(a+b)/2
        print('ID:',DSSV[i]['MaSV'],'HoTen:',DSSV[i]['name'],'co diem trung binh cong la:',round(TB,2))