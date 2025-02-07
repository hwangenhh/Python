#bai 17
import pandas as pd

# Đọc file CSV (giả sử bạn đã lưu file csv_Data_Loan.csv trên máy)
df = pd.read_csv(r"D:\PHYTHON\7.2\bt\data-demo-2.csv")

# Hiển thị dữ liệu
print(df)

#bai 18
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

#bai 28
import pandas as pd

# Đọc toàn bộ file Excel và lấy danh sách các sheet
file_path = r"D:\PHYTHON\7.2\bt\excel_Data_Movies.xls"  # Đường dẫn chính xác
sheets = pd.read_excel(file_path, sheet_name=None)  # Đọc tất cả sheet

# Duyệt qua từng sheet và hiển thị dữ liệu
for sheet_name, df in sheets.items():
    print(f"📄 Sheet: {sheet_name}")
    print(df.head())  # Hiển thị 5 dòng đầu của từng sheet
    print("\n")

#bai 34
import pandas as pd

# Đọc dữ liệu từ file JSON vào DataFrame
file_path = "json_Data_flights.json"  # Thay thế bằng đường dẫn thực tế
data_json = pd.read_json(file_path)

# Hiển thị 5 dòng đầu tiên của DataFrame
print(data_json.head())


#bai 41
import requests
import pandas as pd

# URL API
url = "http://api.plos.org/search?q=title:VIRUS&fl=id,eissn,author_display,abstract,title_display,score"

# Gửi yêu cầu GET đến API
response = requests.get(url)

data = response.json()

# Trích xuất danh sách bài báo
docs = data.get("response", {}).get("docs", [])

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(docs)

# Lưu vào file CSV
df.to_csv("D:\\PHYTHON\\7.2\\bt\Paper.csv", index=False, encoding="utf-8")

print("Dữ liệu đã được lưu vào Paper.csv")

#bai 4_1
import pandas as pd

# Đọc dữ liệu từ file TXT (phân tách bằng tab)
df_lc = pd.read_csv("data_lc.txt", sep="\t")

# Chuyển cột 'Time' thành kiểu datetime
df_lc["Time"] = pd.to_datetime(df_lc["Time"])

# Sắp xếp dữ liệu theo Time giảm dần và lấy 1000 dòng đầu tiên
df_lc = df_lc.sort_values(by="Time", ascending=False).head(1000)

# Hiển thị 10 dòng đầu tiên
print(df_lc.head(10))


#bai 4_2
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
