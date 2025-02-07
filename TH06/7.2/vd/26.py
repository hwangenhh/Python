import pandas as pd

# Tạo DataFrame giống với dữ liệu trong hình
data = {
    'Mã SV': [1621050041, 1621050262, 1621050083, 1621050131, 1621050384],
    'A': [6.7, 6.7, 7.3, 5.7, 7.0],
    'B1': [9.0, 7.0, 8.5, 5.0, 8.0],
    'B2': [5.5, 9.5, 9.0, 10.0, 9.5],
    'C1': [8.5, 8.0, 10.0, 9.0, 10.0],
    'C2': [8.0, 6.0, 9.0, 5.0, 9.0]
}

# Chuyển 'Mã SV' thành index
df = pd.DataFrame(data).set_index('Mã SV')

# Hiển thị DataFrame
print(df)
