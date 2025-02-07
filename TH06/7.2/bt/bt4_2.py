import pymongo
import pandas as pd

# Kết nối MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["demodb"]
collection = db["LC_Meteorology"]

# Truy vấn dữ liệu từ MongoDB
cursor = collection.find(
    {"Id": "LC"},  # Điều kiện lọc
    {"_id": 0, "Time": 1, "Rain": 1, "T2m": 1}  # Chỉ lấy các cột cần thiết
).sort("Time", -1).limit(1000)  # Sắp xếp giảm dần theo Time và lấy 1000 dòng

# Chuyển thành DataFrame
df_lc = pd.DataFrame(list(cursor))

# Chuyển cột 'Time' thành kiểu datetime nếu cần
df_lc["Time"] = pd.to_datetime(df_lc["Time"])

# Hiển thị 10 dòng đầu tiên
print(df_lc.head(10))
