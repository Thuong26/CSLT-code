# viết chương trình nhập vào một xâu ký tự st1.
# nhập vào 1 xâu st2, kiểm tra nếu st2 xuât hiện trong st1 thì yêu 
#cầu nhập lại xâu khác, còn lại thì dùng.
st1=input()
st2=input()
while True:
    if st2 in st1:
        st2=input()
    else: break
