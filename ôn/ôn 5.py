# cho một chuỗi ký tự, viết chương trình để tạ ra một chuỗi mới
# gồm 2 ký tự đầu tiên và 2 ký tự cuối cùng từ chuỗi đã cho. nếu
# chuỗi nhỏ hơn 2 thì trả về chuỗi rỗng.
# input:                                      output
#     Bassic Programming                            Bang 
#     w 
#     an                                            anan
s=input()
l=[]
if len(s)<2:
    print()
else:
    l=s[:2]+s[-2:]
    print(l)