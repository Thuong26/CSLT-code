def quick_sort(s):
    length=len(s)
    if length<=1:
        return s
    else:
        chot=s.pop()
        print (chot)
    lonhon=[]
    bang=[]
    bang.append(chot)
    nhohon=[]
    for i in s:
        if i>chot:
            lonhon.append(i)
        elif(i==chot):
            bang.append(i)
        else:
            nhohon.append(i)
    return quick_sort(nhohon)+(bang)+quick_sort(lonhon)
print(quick_sort([10,20,7,15,3]))