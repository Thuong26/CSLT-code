from re import X
listStudents = []
# Tạo lớp student
class student:
    def __init__(self, id, name, classs, mark1, mark2, average):
        self.id = id
        self.name = name
        self.classs = classs
        self.mark1 = mark1
        self.mark2 = mark2
        self.average = average
def findStudent(id):
    """Hàm tìm một sinh viên"""
    for i in range(0, len(listStudents)):
        if listStudents[i].id == id:
            # Trả về mảng gồm 2 phần tử,
            # 0 là vị trí tìm thấy và 1 là dữ liệu
            return [True, i, id]
    return [False, -1, -1]

def addStudent():
    """Hàm thêm một sinh viên"""
    print("*** THÊM SINH VIÊN ***")
    print('Number of student')
    n = int(input()) 
    for i in range(1,n+1):
        # Nhập ID, có kiểm tra trùng ID thì nhập lại
        print("Nhập ID sinh viên:",i)
        stExist=True
        while stExist:
            id = input()
            stExist = findStudent(id)[0]
        if stExist != False:
            print("ID này đã tồn tại, vui lòng nhập lại:")
        else:
            print("ID này ok",id)
        a = id
        # Nhập tên
        print("Nhập tên sinh viên:",i)
        b = input()
        print("Nhập lớp sinh viên:",i)
        c = input()
        print("Nhập Điểm môn 1:" ,i)
        d = input()
        print("Nhập Điểm môn 2:" ,i)
        e = input()
        # Lưu vào danh sách sv
        z = student(a, b, c, d, e, 0)
        listStudents.append(z)
def deleteStudent():
    """Hàm xóa sih viên"""
    print("*** XÓA SINH VIÊN ***")
    print("Nhập ID sinh viên cần xóa:")
    id = input()

    flag = findStudent(id)[0]

    if flag != False:
        listStudents.remove(listStudents[findStudent(id)[1]])
        print("Xóa sinh viên thành công")
    else :
        print("Không tìm thấy sinh viên cần xóa")
def editStudent():
    """Hàm sửa sinh viên"""
    print("*** SỬA THÔNG TIN SINH VIÊN ***")
    print("Nhập ID sinh viên cần sửa")
    id = input()
    flag = findStudent(id)[0]
    if flag == False:
        print("Không tìm thấy sinh viên ", id)
    else :
        print("Nhập loại thông tin cần sửa (name, class, mark1, mark2)")
        type_info = input()
        update_info = input("Nhập thông tin mới: ")

        if type_info == 'name':
            listStudents[findStudent(id)[1]].name = update_info
        elif type_info == 'class':
            listStudents[findStudent(id)[1]].classs = update_info
        elif type_info == 'mark1':
            listStudents[findStudent(id)[1]].mark1 = update_info
        elif type_info == 'mark2':
            listStudents[findStudent(id)[1]].mark2 = update_info
def showStudents(listStudents):
    """Hàm hiển thị danh sách sv"""
    print("*** DANH SÁCH SINH VIÊN HIỆN TẠI ***")
    print("**[ id ] [ name ] [ class ] [ mark1 ] [ mark2 ] [ average ]**")
    print()
    for i in range(0, len(listStudents)):
        print('[',listStudents[i].id,"]", "[",listStudents[i].name,"]", "[",listStudents[i].classs,"]", "[",listStudents[i].mark1,"]","[",listStudents[i].mark2,"]", "[",listStudents[i].average,"]")


def averageMark():
    for i in range(len(listStudents)):
        listStudents[i].average = (float(listStudents[i].mark1) + float(listStudents[i].mark2)) / 2
    print("Đã tính điểm trung bình của các sinh viên")


def average1():
    a1 = 0
    for i in range (len(listStudents)):
        a1 = a1 + float(listStudents[i].mark1)
    return a1 / len(listStudents)
    
def average2():
    a2 = 0
    for i in range (len(listStudents)):
        a2 = a2+float(listStudents[i].mark2)
    return a2/len(listStudents)


def averageMin():
    min = float(listStudents[0].average)
    x=0
    for i in range(1, len(listStudents)):
        if float(listStudents[i].average) < min:
            min = float(listStudents[i].average)
            x = i
    return x

def averageMax():
    max = float(listStudents[0].average)
    y = 0
    for i in range(1, len(listStudents)):
        if float(listStudents[i].average) > max:
            max = float(listStudents[i].average)
            y = i
    return y


def show_by_class_average():
    listStudents_class_average = []
    for i in listStudents:
        tup = (i.classs, i.average, i.id)
        listStudents_class_average.append(tup)
    
    listStudents_class_average = sorted(listStudents_class_average)

    for i in range(len(listStudents_class_average)):
        for j in range(len(listStudents)):
            if listStudents[j].id == listStudents_class_average[i][-1]:
                listStudents_class_average[i] = listStudents[j]
                break
    return listStudents_class_average
def rank():
    for i in listStudents:
        if i.average >= 9:
            print(i.id, i.name,i.classs,end='')
            print('=> Xuất sắc')
        elif i.average >= 8:
            print(i.id, i.name,i.classs,end='')
            print('=> Giỏi')
        elif i.average >= 6.5:
            print(i.id, i.name,i.classs,end='')
            print('=> Khá')
        elif i.average >= 5:
            print(i.id, i.name,i.classs,end='')
            print('=> Trung bình')
        else:
            print(i.id, i.name,i.classs,end='')
            print('=> Yếu')     
print("Chọn chức năng muốn thực hiện:")
print("1: Thêm sinh viên")
print("2: Xóa sinh viên")
print("3: Sửa sinh viên")
print("4: Xem danh sách sinh viên")
print("5: Tính điểm trung bình học tập cho từng sinh viên (average)")
print("6: Tính điểm trung bình cho môn 1 của toàn bộ sinh viên")
print("7: Tính điểm trung bình cho môn 2 của toàn bộ sinh viên")
print("8: Tìm xem sinh viên nào có điểm trung bình học tập thấp nhất ")
print("9: Tìm xem sinh viên nào có điểm trung bình học tập cao nhất ")
print("10: Sắp xếp danh sách sinh viên theo lớp, nếu trong lớp có nhiều bạn thì sắp xếp từ thấp đến cao theo điểm trung bình hjc tập ")
print("0: Thoát khỏi chương trình")
action = int(input())
while action > 0:
    if action == 1:
        addStudent()
    elif action == 2:
        deleteStudent()
    elif action == 3:
        editStudent()
    elif action == 4:
        showStudents(listStudents)
    elif action == 5:
        averageMark()
    elif action == 6:
        print("Điểm trung bình môn 1 của toàn bộ sinh viên:",average1())
    elif action == 7:
        print("Điểm trung bình môn 2 của toàn bộ sinh viên:",average2())
    if action == 8:
        if listStudents[0].average == 0:
            print("Điểm trung bình chưa được tính.")
            print("Chọn action 5, sau đó quay lại action 8.")
        else:
            x = averageMin()
            print("Sinh viên có điểm trung bình học tập thấp nhất:")
            print("Id, name, class,mark1,mark2,average")
            print(listStudents[x].id,listStudents[x].name, listStudents[x].classs, listStudents[x].mark1,listStudents[x].mark2,listStudents[x].average)
    elif action == 9:
        if listStudents[0].average == 0:
            print("Điểm trung bình chưa được tính.")
            print("Chọn action 5, sau đó quay lại action 9.")
        else:
            y = averageMax()
            print("Sinh viên có điểm trung bình học tập cao nhất:")
            print("Id, name, class,mark1,mark2,average")
            print(listStudents[y].id,listStudents[y].name, listStudents[y].classs, listStudents[y].mark1,listStudents[y].mark2,listStudents[y].average)
    
    elif action == 10:
        if listStudents[0].average == 0:
            print("Điểm trung bình chưa được tính.")
            print("Chọn action 5, sau đó quay lại action 10.")
        else:
            showStudents(show_by_class_average())

    elif action == 11:
        if listStudents[0].average == 0:
            print("Điểm trung bình chưa được tính.")
            print("Chọn action 5, sau đó quay lại action 11.")
        else:
            print('id,name,class =>Rank')
            rank()

    print("Chọn action")
    action = int(input())




