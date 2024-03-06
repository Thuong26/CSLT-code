# Viếtchươngtrình:
# -Nhập vào một chuỗi ký tự chứa họ tên và email;
# -Chương trình thực hiện tách email từ chuỗi trên và in
# kết quả lên màn hình;
# -Biết rằng dữ liệu nhập vào có email hoặc không có email.
# Vídụ:
#         Ho ten: Nguyen Van An, Email: vanan@gmail.com
#         Ho ten: Le Ngoc Binh, Email:
#         Ho ten: Pham Anh Ngoc, Email: anhngoc@gmail.com
# TEST1:
#         Input:Ho ten: Nguyen Van An, Email: vanan@gmail.com
#         Output:vanan@gmail.com
# TEST2:
#         Input:Ho ten: Le Ngoc Binh, Email:
#         Output:
st=input()
if st.find('@')!=-1:
    for i in range(len(st)-1,0,-1):
        if st[i]==' ':
            print(st[i+1:])
            break
else:
    print()