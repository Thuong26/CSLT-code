# a=int(input('a='))
# b=int(input('b='))
# print('a+b=',a+b)

# Nhập các hệ số từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    print("Phương trình có hai nghiệm thực phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2 * a)
    print("Phương trình có nghiệm kép:")
    print("x =", x)
else:
    print("Phương trình vô nghiệm")
