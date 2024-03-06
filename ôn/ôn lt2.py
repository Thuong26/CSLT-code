# Biểu diễn chuỗi ký tự
#  Xử dụng cặp dấu nháy đơn ‘’ hoặc nháy kép “” để biểu diễn 
# một chuỗi ký tự
# Hiển thị ký tự đặc biệt với dấu \
#     \' 
#     \"
#     \t
#     \n
#      \\
# Định nghĩa chuỗi dữ liệu thô(rawstring)
# Đặt ký tự r trước dấu “hoặc‘ bắt đầu chuỗi, để giữ lại các ký
# tự đặc biệt trong chuỗi.
# Biểu diễn chuỗi gồm nhiều dòng văn bản 
# Sử dụng 3 dấu nháy đơn ‘’’ bắt đầu và kết thúc khối văn bản để
# biểu diễn chuỗi gồm nhiều dòng.

# Phương thức upper(),lower()
# Trả về một chuỗi được viết hoa hoặc viết thường;

# Phươngthứcisupper(),islower()
# Trả về true hoặc false nếu một chuỗi (chữcái) có được viết hoa
# hay viết thường toàn bộ xâu;

# Phương thức isalpha()
# isalpha(): trả về True nếu chuỗi chỉ chứa các ký tự chữ cái và 
# không có ký tự trắng,còn lại trả về False;

# Phương thức isnumeric(),isdecimal()
# Trả về True nếu chuỗi chỉ chứa các ký tự chữ số và không có ký 
# tự trắng,còn lại trả về False;

# Phương thức isalnum()
# isalnum():trả về True nếu chuỗi chỉ chứa các ký tự chữ cái,
# chữ số và không có ký tự trắng, còn lại trả về False;

# isspace(): trả về True nếu chuỗi chỉ chứa kí tự trắng hoặc dấu 
# tab, hoặc dấu ngắt dòng, còn lại trả về False

# istitle():trả về True nếu chuỗi chỉ chứa các từ, mỗi từ được 
# viết thường và viết hoa chữ cái đầu, còn lại trả về False;

# Phương thức startswith(str), endswith(str)
# startswith(str):Trả về True nếu chuỗi bắt đầu bởi chuỗi str,
# còn lại trả về False;
# endswith(str): Trả về True nếu chuỗi kết thúc bởi chuỗi str,
# còn lại trả về False;

# Phương thức join(ListOfString)
# join(ListOfString):ListOfString là một List gồm các chuỗi ký tự
# .join() dùng để nối các phần tử trong ListOfString bằng một 
# chuỗi tương ứng của phương thức;

# Phương thức rjust(n,ch), ljust(n,ch), center(n,ch)
# Trả về một chuỗi mới khi thêm vào chuỗi gốc các ký tự ch,
# sao cho chiều dài của chuỗi đúng bằng n ký tự và chuỗi gốc được 
# đặt nằm bên phải (rjust()), bêntrái(ljust()) hoặc ở giữa (center());
# vd 'hello'.rjust(10): thêm 5 kí tự trắng vào bên trái chuỗi gốc
# '    hello'

# Phương thức strip(str), rstrip(str), and lstrip(str) 
# Trả về một chuỗi mới trong đó đã xóa các ký tự có trong 
# chuỗi str ở 2 đầu (strip()),bên phải(rstrip()) 
# hoặc bên trái(lstrip())chuỗigốc.

# Phương thức find(str,n)Thựchiệntìmchuỗi str 
# trongchuỗigốc,bắt đầu từ kýtựcósốchỉmụcn,
# nđểtrốngthìmặcđịnhbằng0.Trảvềvịtrí(index)lầnđầu
# đượctìmthấy(từtráisangphải).Nếukhôngtìmthấythìtrảvề-1.

# Phương thức replace(oldvalue, newvalue, n)
# Tìmvàthaythếcácchuỗioldvaluexuấthiệntrongchuỗigốcbằng
# newvalue,vớinlầntìmvàthaythế;
# Nếukhôngcón:thìmặcđịnhlàtấtcảcáclầnxuấthiện.