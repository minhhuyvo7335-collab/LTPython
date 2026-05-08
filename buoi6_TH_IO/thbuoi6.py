# =========================
# BƯỚC 1: ĐỌC FILE VĂN BẢN
# =========================

with open("fileName.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Nội dung file gốc:\n")
print(text)


# =========================
# BƯỚC 2: GIẢM DUNG LƯỢNG
# =========================

dictionary = []
positions = []

for char in text:

    if char not in dictionary:
        dictionary.append(char)

    positions.append(dictionary.index(char))


# Ghi file nén
with open("compressed.txt", "w", encoding="utf-8") as f:

    f.write("".join(dictionary))
    f.write("\n")

    for pos in positions:
        f.write(str(pos) + " ")

print("\nĐã tạo file compressed.txt")


# =========================
# BƯỚC 3: ĐỌC FILE ĐÃ NÉN
# =========================

with open("compressed.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

dictionary = list(lines[0].rstrip("\n"))
positions = list(map(int, lines[1].split()))


# =========================
# BƯỚC 4: KHÔI PHỤC VĂN BẢN
# =========================

restored_text = ""

for pos in positions:
    restored_text += dictionary[pos]


# Ghi file khôi phục
with open("restored.txt", "w", encoding="utf-8") as f:
    f.write(restored_text)

print("\nĐã tạo file restored.txt")


# =========================
# BƯỚC 5: HIỂN THỊ KẾT QUẢ
# =========================

with open("restored.txt", "r", encoding="utf-8") as f:
    result = f.read()

print("\nNội dung sau khi khôi phục:\n")
print(result)