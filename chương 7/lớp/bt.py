# nhập vào một chuỗi kí tự làm mật khẩu  cho chương trình
# yêu cầu
# mật khẩu có 8 kí tự
# bao gồm: chữ cái, chữ số, chữ viết hoa và viết thường
# nếu không hợp lệ thì yêu cầu nhập lại
while True:
    mk=input()
    if len(mk)<8 or mk.isupper() or mk.islower() or mk.isnumeric() or mk.isalpha():
        print('Khong hop le')
    elif mk.isalnum() and len(mk)>=8:
        print('Hop le')
        break
    else:
        print('Khong hop le')

