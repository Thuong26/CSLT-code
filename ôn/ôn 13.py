# Viết chương trình để kiểm tra các ký tự không mong muốn khỏi 
# một chuỗi đã cho. Biết rằng, các ký tự không mong muốn 
# gồm:'#,',!,^,%'
# input:
#   Pyth^on Exercis^es
# output:
#   Python Exercises
n=input()
L=list(n)
for i in L:
    if "*" in L:
        L.remove("*")
    if "^" in L:
        L.remove("^")
    if "@" in L:
        L.remove("@")
    if "&" in L:
        L.remove("&")  
M="".join(L)
print(M)