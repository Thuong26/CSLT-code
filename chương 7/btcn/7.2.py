#  Viết chương trình:
#  -Cho phép nhập vào một chuỗi ký tự bất kỳ;
#  Chương trình thực hiện làm sạch chuỗi ký tự trên. 
#  Biết rằng một chuỗi được gọi là “sạch” nếu: 
#     + Không bắt đầu và kết thúc bằng các ký tự trắng;
#     + Mỗi từ chỉ được cách nhau bằng đúng 1 ký tự trắng;
#     + Chỉ được phép viết hoa chữ cái đầu tiên của chuỗi;
#     + Trước các dấu câu (phẩy, chấm phẩy, hai chấm, chấm) không có ký tự trắng;
# -In nội dung chuỗi sau khi xử lý lên màn hình.
# TEST:
# Input:Xin Chào , tôi là    sInh viêN
# Output:Xin chào, tôi là sinh viên
# n=input()
# h=n.strip()
# str=''
# for i in range(len(h)):
#     if (h[i]==' ' and h[i+1]==' ')or(h[i]==' ' and h[i+1]==',') or (h[i]==' ' and h[i+1]==';') or (h[i]==' ' and h[i+1]==':') or (h[i]==' ' and h[i+1]=='.') :
#         continue 
#     str=str+h[i].lower()
# print(str.capitalize())
st=input().strip()
s=''
for i in range(len(st)):
    if (st[i]==' ' and st[i+1]==',') or (st[i]==' ' and st[i+1]==';') or (st[i]==' ' and st[i+1]==':') or (st[i]==' ' and st[i+1]=='.') :
        continue
    s=s+st[i]
s=' '.join(s.split())
print(s.capitalize())
