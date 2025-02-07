import pandas as pd

# Đường dẫn file CSV
file_path = "data.csv"  # Thay thế bằng đường dẫn thực tế của bạn

# Đọc dữ liệu từ file CSV với cột đầu tiên làm index
data = pd.read_csv(file_path, index_col=0)

# Hiển thị thông tin về dữ liệu
data.info()

# Hiển thị 5 dòng đầu tiên
data.head()
