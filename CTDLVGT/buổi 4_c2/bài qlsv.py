# from ast import Delete
# class SinhVien:
#     def __init__(self,MaSV,name,classs,d1,d2):
#         self.MaSV = MaSV
#         self.name = name
#         self.classs = classs
#         self.diem1 = d1
#         self.diem2 = d2
#         self.TB = 0
        
# DSSV=[]
# def addSV():
#     infor={ 'MaSV' : '',
#             'name' : '',
#             'class' : '',
#             'diem1' : '',
#             'diem2' : '',
#         }
#     MaSV=input("Nhap ma SV : ")
#     while True:
#         k=0
#         for i in range(len(DSSV)):
#             if DSSV[i]['MaSV']!=MaSV:
#                 k=k+1
#         if len(DSSV)==0:
#             break
#         elif k==len(DSSV):
#             break
#         else:
#             print("Ma ID da ton tai")
#             MaSV=input("Nhap ma ID cua sinh vien:") 
#     infor['MaSV']=MaSV
#     name=input("Nhap ho ten:")
#     infor['name']=name
#     classs=input("Nhap lop:")
#     infor['class']=classs
#     d1=float(input("Nhap mark1:"))
#     infor['diem1']=d1
#     d2=float(input("Nhap mark2:"))
#     infor['diem2']=d2
#     DSSV.append(infor)
#     print("Them vao thanh cong")
# #Cau 2: Xoa sinh vien
# def delsv():
#     MaSV=input("Nhap ma ID cua sinh vien can xoa:")
#     i=0
#     k=0
#     while True:
#         i=0
#         while i<len(DSSV):
#             if DSSV[i]['MaSV']==MaSV:
#                 DSSV.remove(DSSV[i])
#                 k=1
#                 break
#             i=i+1
#         if k==1:
#             break 
#         else:
#             print("khong tim thay id")
#             MaSV=input("Nhap ma ID cua sinh vien can xoa:") 
# #3 sua sinh vien
# def editsv():
#     MaSV=input("Nhap ma ID cua sinh vien can sua chua thong tin:")
#     k=0
#     while True:
#         for i in range(len(DSSV)):
#             if DSSV[i]['MaSV']==MaSV:
#                 name=input("Nhap ho ten:")
#                 DSSV[i]['name']=name
#                 classs=input("Nhap lop:")
#                 DSSV[i]['class']=classs
#                 d1=float(input("Nhap mark1:"))
#                 DSSV[i]['diem1']=d1
#                 d2=float(input("Nhap mark2:"))
#                 DSSV[i]['diem2']=d2
#                 k=1
#         if k==0:
#             print("khong tim thay id")
#             MaSV=input("Nhap ma ID cua sinh vien can sua chua thong tin:")      
#         elif k==1:
#             break
# #Cau 4: in
# def printsv():
#     for i in range(len(DSSV)):
#         print(DSSV[i])
# #Cau 5: tinh diem trung binh
# def avesv():
#     for i in range (len(DSSV)):
#         a=DSSV[i]['diem1']
#         b=DSSV[i]['diem2']
#         TB=(a+b)/2
#         print('ID:',DSSV[i]['MaSV'],'HoTen:',DSSV[i]['name'],'co diem trung binh cong la:',round(TB,2))
# #Cau 6: Tính điểm trung bình cho môn 1 của toàn bộ sinh viên: averageMark1
# def avm1():
#     dem=0
#     tong=0
#     for i in range (len(DSSV)):
#         dem=dem+1
#         tong=tong+DSSV[i]['d1']
#     print('mark 1 co diem trung binh cong la:',round(tong/dem,2))
# #Cau 7: Tính điểm trung bình cho môn 2 của toàn bộ sinh viên : averageMark2
# def avm2():
#     dem=0
#     tong=0
#     for i in range (len(DSSV)):
#         dem=dem+1
#         tong=tong+DSSV[i]['diem1']
#     print('mark 2 co diem trung binh cong la:',round(tong/dem,2))
# #Cau 8: Tìm xem sinh viên nào có điểm trung bình học tập thấp nhất, in ra toàn bộ thông tin của SV đó
# def avemin():
#     min=11
#     for i in range (len(DSSV)):
#         a=DSSV[i]['diem1']
#         b=DSSV[i]['diem2']
#         ave=(a+b)/2
#         if min>ave:
#             min=ave
#             k=i
#     if ave!=0:
#         print('ID:',DSSV[k]['MaSV'],', HoTen:',DSSV[k]['name'],', Lop:',DSSV[k]['class'],', Mark 1:',DSSV[k]['diem1'],', Mark 2:',DSSV[k]['diem2'],', co diem trung binh cong thap nhat=',round(min,2))
#     else: 
#         print("Điểm trung bình chưa được tính.")
#         print("Chọn action 5, sau đó quay lại action 8.")
# #Cau 9: Tìm xem sinh viên nào có điểm trung bình học tập cao nhất, in ra toàn bộ thông tin của SV đó 
# def avemax():
#     max=0
#     for i in range (len(DSSV)):
#         a=DSSV[i]['diem1']
#         b=DSSV[i]['diem2']
#         ave=(a+b)/2
#         if max<ave:
#             max=ave
#             k=i
#     if ave!=0:
#         print('ID:',DSSV[k]['MaSV'],', HoTen:',DSSV[k]['name'],', Lop:',DSSV[k]['class'],', Mark 1:',DSSV[k]['diem1'],', Mark 2:',DSSV[k]['diem2'],', co diem trung binh cong cao nhat=',round(max,2))
#     else: 
#         print("Điểm trung bình chưa được tính.")
#         print("Chọn action 5, sau đó quay lại action 9.")
# print('0: Thoat chuong trinh \n1: Thêm sinh viên \n2: Xóa sinh viên \n3: Sửa sinh viên4: Xem danh sách sinh viên \n5: Tính điểm trung bình học tập cho từng sinh viên (average= (mark1+mark2)/2 \n6: Tính điểm trung bình cho môn 1 của toàn bộ sinh viên: averageMark1 \n7: Tính điểm trung bình cho môn 2 của toàn bộ sinh viên : averageMark2 \n8: Tìm xem sinh viên nào có điểm trung bình học tập thấp nhất, in ra toàn bộ thông tin của SV đó \n9: Tìm xem sinh viên nào có điểm trung bình học tập cao nhất, in ra toàn bộ thông tin của SV đó ')
# action=1
# while action!=0:
#     action=int(input("Nhap:"))
#     if action==1:
#         addSV()
#     elif action==2:
#         delsv()
#     elif action==3:
#         editsv()
#     elif action==4:
#         printsv()
#     elif action==5:
#         avesv()
#     elif action==6:
#         avm1()
#     elif action==7:
#         avm2()
#     elif action==8:
#         avemin()
#     elif action==9:
#         avemax()