import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv(r"D:\PHYTHON\7.2\bt\data-demo-2.csv")  # Thay thế bằng đường dẫn thực tế

# Tách các cột dữ liệu số (numerical)
df_number = df.select_dtypes(include=['number'])

# Tách các cột dữ liệu dạng object (chuỗi, category)
df_object = df.select_dtypes(include=['object'])

# Hiển thị kết quả
print("Dữ liệu số:")
print(df_number.head())

print("\nDữ liệu object:")
print(df_object.head())