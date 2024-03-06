# viết chương trình nhập vào một xâu ký tự st1.
# nhập vào 1 xâu st2, kiểm tra nếu st2 xuât hiện trong st1 thì yêu 
#cầu nhập lại xâu khác, còn lại thì dùng.'không phân biệt chữ hoa chữ thường'
st1=(input()).lower
st2=(input()).lower
while True:
    if st2 in st1:
        st2=(input()).lower
    else: break
