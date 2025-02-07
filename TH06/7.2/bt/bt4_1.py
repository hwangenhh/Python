import pandas as pd

# Đọc dữ liệu từ file TXT (phân tách bằng tab)
df_lc = pd.read_csv("data_lc.txt", sep="\t")

# Chuyển cột 'Time' thành kiểu datetime
df_lc["Time"] = pd.to_datetime(df_lc["Time"])

# Sắp xếp dữ liệu theo Time giảm dần và lấy 1000 dòng đầu tiên
df_lc = df_lc.sort_values(by="Time", ascending=False).head(1000)

# Hiển thị 10 dòng đầu tiên
print(df_lc.head(10))
