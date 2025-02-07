import pandas as pd

# Đường dẫn file CSV
path = "data.csv"  # Thay thế bằng đường dẫn thực tế của bạn

# Đọc dữ liệu từ file CSV
data = pd.read_csv(path)

# Hiển thị thông tin về dữ liệu
data.info()

