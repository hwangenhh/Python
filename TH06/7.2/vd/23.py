import pandas as pd

# Đọc dữ liệu từ file JSON
path_json = "data.json"
data_ex1 = pd.read_json(path_json)

# Hiển thị thông tin của DataFrame
data_ex1.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex1.head()
