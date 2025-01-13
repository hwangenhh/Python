import csv
import random
from datetime import datetime, timedelta

# Danh sách thành phố
cities = ["Hà Nội", "Vinh", "Đà Nẵng", "Nha Trang", "Hồ Chí Minh", "Cà Mau"]

# Thời gian bắt đầu và kết thúc
start_time = datetime(2019, 9, 15, 0, 0)
end_time = datetime(2019, 9, 22, 23, 0)

# Tạo file CSV
file_name = "temp_data.txt"
with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Viết header
    writer.writerow(["Thời gian"] + cities)
    
    # Viết dữ liệu
    current_time = start_time
    while current_time <= end_time:
        row = [current_time.strftime("%d/%m/%Y %H:%M")]
        # Sinh nhiệt độ ngẫu nhiên từ 20 đến 35 độ C cho mỗi thành phố
        row.extend([round(random.uniform(20, 35), 1) for _ in cities])
        writer.writerow(row)
        current_time += timedelta(hours=1)

print(f"File '{file_name}' đã được tạo thành công.")
