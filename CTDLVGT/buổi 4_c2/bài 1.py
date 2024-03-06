class student:
     def __init__(self, id, name, mark1, mark2, grade):
          self.id=id
          self.name=name
          self.mark1=mark1
          self.mark2=mark2
          self.grade=grade

     def xuatsv(self):
          print(self.id,self.name,self.mark1,self.mark2,self.grade)

     def dtb(self):
          self.average=(self.mark1+self.mark2)/2
          return self.average

     def xeploai(self):
          if self.dtb()>=9: self.loai="xuat sac"
          elif self.dtb()>=8: self.loai="gioi"
          elif self.dtb()>=6.5: self.loai="kha"
          elif self.dtb()>=5: self.loai="trung binh"
          else: self.loai="yeu"
          return self.loai

class ds:
     ds=[]
     # ds=[student(1,"trieu",float(5),float(6),"a"),student(2,"hoang",float(6),float(7),"b"),student(3,"minh",float(3),float(4),"a"),student(4,"viet",float(9),float(3),"b")]
     def them(self):
          print("nhap sinh vien: ")
          while True:
               id=int(input("id="))
               name=input("name=")
               mark1=float(input("mark1="))
               mark2=float(input("mark2="))
               grade=input("grade=")
               tam=student(id,name,mark1,mark2,grade)
               self.ds=self.ds+[tam]
               tt=input("nhap t de tiep tuc nhap: ")
               if tt!='t': break
               # i=i+1
          print()

     def xoa(self):
          print("xoa sinh vien: ")
          while True:
               idxoa=int(input("id="))
               for i in range(len(self.ds)):
                    if self.ds[i].id==idxoa:
                         del self.ds[i]
                         break
               tt=input("nhap t de tiep tuc xoa: ")
               if tt!='t': break
               # i=i+1
          print()

     def sua(self):
          print("sua thong tin sinh vien: ")
          while True:
               idsua=int(input("id="))
               for i in range(len(self.ds)):
                    if self.ds[i].id==idsua:
                         self.ds[i].xuatsv()
                         name=input("name=")
                         mark1=float(input("mark1="))
                         mark2=float(input("mark2="))
                         grade=input("grade=")
                         self.ds[i]=student(idsua, name, mark1, mark2,grade)
                         break
               tt=input("nhap t de tiep tuc sua: ")
               if tt!='t': break
               # i=i+1
          print()

     def xuat(self):
          print("danh sach sinh vien: ")
          if self.ds!=[]:
               for i in self.ds:
                    i.xuatsv()
                    # print(i.id,i.name,i.mark1,i.mark2,i.grade)
          print()

     def xuatdtb(self):
          print("diem tb hoc tap: ")
          for i in self.ds:
               print(i.id,i.name,i.dtb())
          print()
     
     def xuatdtbmark1(self):
          print("diem tb mon 1: ",end="")
          dtb=0
          for i in self.ds:
               dtb=dtb+i.mark1
          dtb=dtb/len(self.ds)
          print(dtb)
          print()

     def xuatdtbmark2(self):
          print("diem tb mon 2: ",end="")
          dtb=0
          for i in self.ds:
               dtb=dtb+i.mark2
          dtb=dtb/len(self.ds)
          print(dtb)
          print()   

     def xuatdtbmin(self): 
          min=self.ds[0].dtb()
          imin=0
          for i in range(len(self.ds)):
               if self.ds[i].dtb()<min:
                    min=self.ds[i].dtb()
                    imin=i
          self.ds[imin].xuatsv()
          print("co diem tb thap nhat la "+str(self.ds[imin].dtb()))
          print()

     def xuatdtbmax(self): 
          max=self.ds[0].dtb()
          imax=0
          for i in range(len(self.ds)):
               if self.ds[i].dtb()>max:
                    max=self.ds[i].dtb()
                    imax=i
          self.ds[imax].xuatsv()
          print("co diem tb cao nhat la "+str(self.ds[imax].dtb()))
          print()

     def sapxep(self):
          L=[]
          dsmoi=[]
          dstt=[]
          for i in self.ds:
               if i.grade not in L:
                    L=L+[i.grade]
                    dstt=[]
                    for t in self.ds:
                         if t.grade==i.grade:
                              dstt=dstt+[t]
                    for t in range(0, len(dstt) - 1):
                         for j in range(t + 1, len(dstt)):
                              if (dstt[t].dtb() > dstt[j].dtb()):
                                   tam = dstt[t]
                                   dstt[t] = dstt[j]
                                   dstt[j] = tam
                    for t in dstt:
                         dsmoi=dsmoi+[t]
          self.ds=dsmoi

     def xuatxeploai(self):
          for i in self.ds:
               print(i.id,i.name,i.xeploai())
          print()
qlsv=ds()
print('''
     +--------------------------------------------+
     |         PHAN MEM QUAN LY HOC TAP           |
     |                        by group 6          |
     |                                            |
     |   Nhap so tac vu:                          |
     |   1. Them sinh vien                        |
     |   2. Xoa sinh vien                         |
     |   3. Sua thong tin sinh vien               |
     |   4. Xem danh sach sinh vien               |
     |   5. Tinh diem trung binh hoc tap          |
     |   6. Tinh diem trung binh mon 1            |
     |   7. Tinh diem trung binh mon 2            |
     |   8. Kiem tra sinh vien co dtb thap nhat   |
     |   9. Kiem tra sinh vien co dtb cao nhat    |
     |   10. Sap xep danh sach sinh vien          |
     |   11. Xep loai hoc luc cua sinh vien       |
     |   0. Ket thuc                              |
     +--------------------------------------------+
''')
while True:
     tt=int(input("Nhap: "))
     print()
     if tt==1: qlsv.them()
     elif tt==2: qlsv.xoa()
     elif tt==3: qlsv.sua()
     elif tt==4: qlsv.xuat()
     elif tt==5: qlsv.xuatdtb()
     elif tt==6: qlsv.xuatdtbmark1()
     elif tt==7: qlsv.xuatdtbmark2()
     elif tt==8: qlsv.xuatdtbmin()
     elif tt==9: qlsv.xuatdtbmax()
     elif tt==10: qlsv.sapxep()
     elif tt==11: qlsv.xuatxeploai()
     else: break
     a=input("nhap enter de tiep tuc")
     print("     +--------------------------------------------+")