# Số chỉ mục (index):
#  Có thể truy xuất đến các phần tử trong List thông qua số 
# chỉ mục (index);
#  Index bắt đầu từ số 0 (zero), phần tử thứ n trong List sẽ có
# index là (n-1);
#  Sử dụng tên biến và số index để truy xuất;

# Truy xuất tập con trong List
# Slice: khung trượt (cửa sổ trượt) cho phép truy xuất được
# đồng thời nhiều phần tử trong list
# spam=['cat','bat','rat','elephant']
# spam[0:4]: tập con từ index=0 -> index=3
# spam[1:3]: tập con từ index=1 -> index=2
# spam[0:-1]: tập con từ index=0 -> ptu áp cuối

# Toán tử in và not 
#  Toán tử in và not giúp xác định một giá trị có tồn tại 
# trong một List hay không;
#  Biểu thức trả về True(có) hoặcFalse(không);

# Hàm max()
# Trả về phần tử có giá trị lớn nhất trong List
#   print(max(s))
# Hàm min()
# Trả về phần tử có giá trị bé nhất trong List

# Xóa phần tử trong List với hàm del()
# sp=[1,2,3,4,5]
# del(sp[1])

# Duyệt các phần tử trong List
# 1. for x in s: print(x,end=' ')
# 2. for x in range(len(s)): 

# index() method
#  Trả về index của một phần tử được tìm thấy trong List;
#  Trong trường hợp x không tồn tại trong List sẽ bị lỗi
#  cần sử dụng cú pháp:if x in L để kiểm tra trước 
# khi gọi phương thức index().

# append(), insert()method
#  append(x) thêm phần tử x vào cuối List;
#  insert(i,x) chèn x vào vị trí i hiện có trong List;

# remove()method
#     remove(x):xóa phần tử x đầu tiên tìm thấy trong List;
#     Trong trường hợp x không tồn tại trong List sẽ bị lỗi
#     cần sử dụng cú pháp:if x in L để kiểm tra trước khi 
#     gọi phương thức remove().

# remove()method
#       Phân biệt giữa hàm del()và phương thức remove()
#        ‐Hàm del()xóa một phần tử khi biết index
#        ‐Hàm remove() xóa một phần tử khi biết giá trị

# sort()method : Hàm sort()chỉ thực hiện được khi các phần tử có cùng kiểu dữ liệu
#       Mặc định sắp xếp tăng dần, thêm tham số 
#       reverse=True để sắp xếp giảm dần;
#       s.sort(): tang dan 
#       s.sort(reverse=True): giam dan 

# reverse() method
#    Thực hiện đảo ngược thứ tự các phần tử trong List
#    l.reverse()

# clear()
#        Thực hiện xóa tất cả các phần tử trong List
#        l.clear()

# count(x)
#     Thực hiện đếm số phần tử xxuất hiện trong List
#      l.count(4)

# copy()
#       Thực hiện tạo ra một bản sao mới của List
#       l=k.copy()

# pop(i)
#     Thực hiện xóa và lấy ra giá trị của phần tử có số chỉ mục itrong List. 
#     Nếu tham số i để trống thì mặc định là lấy phần tử cuối trong List.
#     l.pop()
