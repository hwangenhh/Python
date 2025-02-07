import pandas as pd

# Đọc dữ liệu từ file JSON vào DataFrame
file_path = "json_Data_flights.json"  # Thay thế bằng đường dẫn thực tế
data_json = pd.read_json(file_path)

# Hiển thị 5 dòng đầu tiên của DataFrame
print(data_json.head())
