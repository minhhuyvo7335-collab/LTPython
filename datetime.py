#caui
from datetime import datetime
now = datetime.now()
info = {
    "Năm": now.year,
    "Tháng (chữ)": now.strftime("%B"),
    "Tuần trong năm": now.isocalendar().week,
    "Tuần trong tháng": (now.day - 1)//7 + 1,
    "Ngày trong năm": now.timetuple().tm_yday,
    "Ngày": now.day,
    "Thứ": now.strftime("%A"),
    "Giờ": now.strftime("%H:%M:%S")
}
print("\n".join(f"{k}: {v}" for k, v in info.items()))

 #cauii
from datetime import datetime
d1, d2 = [datetime.strptime(input(f"Nhập ngày {i} (dd/mm/yyyy): "), "%d/%m/%Y") for i in (1,2)]
print("Số ngày cách nhau:", abs((d2 - d1).days))

#cauiii
from datetime import datetime
print(datetime.strptime(input("Nhập chuỗi: "), "%b %d %Y %I:%M%p"))

#cauiv
from datetime import datetime, timedelta
print((datetime.now() + timedelta(seconds=5)).strftime("%H:%M:%S"))