# Hệ thống Elearning của Trường Đại học Kinh tế, Đại học Đà Nẵng cho phép người dùng 
# đổi mật khẩu khi cần thiết. Để đảm bảo tính an toàn và bảo mật thông tin cho sinh viên,
# hệ thống yêu cầu mật khẩu phải được đáp ứng các yếu tố an toàn. Bạn hãy viết chương trình
# để thực hiện kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào. Biết rằng, chính sách mật khẩu 
# được quy định như sau:
# -Ít nhất 1 chữ cái nằm trong [a-z]
# -Ít nhất 1 số nằm trong [0-9]
# -Ít nhất 1 kí tự nằm trong [A-Z]
# -Ít nhất 1 ký tự nằm trong [$ # @]
# -Độ dài mật khẩu tối thiểu: 6 ký tự-Độ dài mật khẩu tối đa: 17 ký tự
s=input()
kt=False
dk1=False
dk2=False
if 6<=len(s)<=17 and s.isupper()==False and s.islower()==False:
    for i in s:
        if i.isdecimal()==True:
            dk1=True
        if i=='@' or i=='#' or i=='$':
            dk2=True
    if dk1== True and dk2== True:
        kt=True
if kt==True: print('True')
else: print('False')