#Cho đoạn truyện Kiều như sau:
#"--Người---đâu-gặp---gỡ-làm-chi---
#Trăm----năm-biết-có---duyên---gì--hay--không.
#Ngổn-ngang---trăm-mối---bên---lòng----
#----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình."

#Yêu cầu tiền xử lý, để thành đoạn văn bản có ý nghĩa.
#"Người đâu gặp gỡ làm chi 
#Trăm năm biết có duyên gì hay không.
#Ngổn ngang trăm mối bên lòng
#Nên câu tuyệt diệu ngụ trong tính tình."
sp='''"--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình."'''
L=sp.split('\n')
for i in range(len(L)):
    s=' '.join(L[i].split('-')) 
    s=' '.join(s.split())
    print()