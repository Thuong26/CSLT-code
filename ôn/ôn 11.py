# cho n kí tư, viết chương trình để tính tổng các chữ số có 1 chữ 
# số trong chuỗi. Nếu dấu trừ đứng trước 1 số thì vẫn tính đó là
# số âm.
# input: 123abcd45
# output: 15
# input: 1-2-3abcd45
# output: 5
S=input()
t=i=0
while i<len(S):
    if S[i]=='-':
        i=i+1
        t=t-int(S[i])
    elif S[i].isdecimal():
        t=t+int(S[i])
    i=i+1
print(t)    
