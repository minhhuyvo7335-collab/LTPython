n = int(input("Nhập n: "))
chan = le = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        chan += 1
    else:
        le += 1
    n //= 10

print("Số lượng số chẵn:", chan)
print("Số lượng số lẻ:", le)