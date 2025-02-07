import pandas as pd

# Đường dẫn tới file Excel
file_path = "Data_Exercise/Data_Excel.xlsx"  # Thay thế bằng đường dẫn thực tế

# Đọc dữ liệu từ file Excel
data = pd.read_excel(file_path)

# Hiển thị 5 dòng đầu tiên
print(data.head())
