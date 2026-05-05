from collections import Counter
S1 = input("Nhập S1: ")
S2 = input("Nhập S2: ")
# Câu A
ketqua = list((Counter(S1) & Counter(S2)).keys())
print("Các ký tự xuất hiện trong cả 2 chuỗi:", ketqua)
# Câu B
set1, set2 = set(S1), set(S2)
kyturiengS1 = [c for c in set1 if c not in set2]
kyturiengS2 = [c for c in set2 if c not in set1]
tong = len(kyturiengS1) + len(kyturiengS2)
print("Số ký tự chỉ xuất hiện ở một trong hai chuỗi:", tong)
# Câu C
dict1, dict2 = dict(Counter(S1)), dict(Counter(S2))
print("Ký tự có trong S1 nhưng không có trong S2:",
      [k for k in dict1 if k not in dict2])
print("Ký tự có trong S2 nhưng không có trong S1:",
      [k for k in dict2 if k not in dict1])

      