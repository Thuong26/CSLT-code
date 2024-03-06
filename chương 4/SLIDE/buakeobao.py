import random

def nhap_so_nguyen():
    while True:
        n = int(input("Human:"))
        if n in [0, 1, 2, 3]:
            return n
        else:
            print("Số nhập vào không hợp lệ. Vui lòng nhập lại.")

def sinh_so_ngau_nhien():
    return random.randint(1, 3)

def kiem_tra_ket_qua(n, m):
    if n == m:
        return "Draw"
    elif (n == 1 and m == 3) or (n == 2 and m == 1) or (n == 3 and m == 2):
        return "Human win"
    else:
        return "Computer win"

while True:
    human = nhap_so_nguyen()
    if human == 0:
        print("Đã dừng chương trình.")
        break

    computer = sinh_so_ngau_nhien()
    print("Computer:", computer)

    result = kiem_tra_ket_qua(human, computer)
    print("Result:", result)
    print()
