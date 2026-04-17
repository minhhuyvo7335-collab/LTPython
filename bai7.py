n = int(input("Nhập n: "))
temp = n
flag = True

while temp > 0:
    digit = temp % 10
    if digit != 6 and digit != 8:
        flag = False
        break
    temp //= 10

if flag:
    print(n, "là số may mắn")
else:
    print(n, "KHÔNG phải số may mắn")