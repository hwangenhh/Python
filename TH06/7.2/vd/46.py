import pandas as pd

# Dữ liệu giả lập
data_mg = [
    {"Time": "2018-12-31 00:00:00", "Rain": 2.6, "T2m": 9.7, "Tm": 8.3, "Tx": 11.6},
    {"Time": "2018-12-30 00:00:00", "Rain": 1.9, "T2m": 9.4, "Tm": 8.1, "Tx": 11.6},
    {"Time": "2018-12-29 00:00:00", "Rain": 4.3, "T2m": 10.2, "Tm": 8.4, "Tx": 12.3},
    {"Time": "2018-12-28 00:00:00", "Rain": 0.0, "T2m": 8.0, "Tm": 7.0, "Tx": 10.4},
    {"Time": "2018-12-27 00:00:00", "Rain": 0.0, "T2m": 17.0, "Tm": 12.0, "Tx": 25.8},
]

# Chuyển thành DataFrame
df = pd.DataFrame(data_mg)

# Hiển thị thông tin và 5 dòng đầu tiên
df.info()
print(df.head())
