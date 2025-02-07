import pandas as pd

# Đường dẫn file CSV
file_path = "data.csv"  # Thay thế bằng đường dẫn thực tế của bạn

# Đọc dữ liệu từ file CSV với cột đầu tiên làm index
data2 = pd.read_csv(file_path, 
                    nrows=100,
                    usecols=['Height_cm','Weight_kg'])

# Hiển thị thông tin về dữ liệu
data2.info()

# Hiển thị 5 dòng đầu tiên
data2.head()
