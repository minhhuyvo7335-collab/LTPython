# Câu III
S = input("Nhập số điện thoại: ")

khong_co = {str(i) for i in range(10)} - set(S)

print("Các số không xuất hiện:", khong_co)

#Câu IV
S = input("Nhập chuỗi: ")

da_xuat_hien = set()
ket_qua = None

for tu in S.split():
    if tu in da_xuat_hien:
        ket_qua = tu
        break
    da_xuat_hien.add(tu)

print(ket_qua)


