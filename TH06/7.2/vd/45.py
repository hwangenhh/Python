import pymongo as mg

# Thiết lập tham số kết nối
address = "118.70.196.130:27017"
user = "root"
pas = "Humg@123mg"
auth = "SCRAM-SHA-1"
database = "Data_Laichau"
coll_name = "LC_Meteorology"

# Kết nối tới CSDL MongoDB
client = mg.MongoClient(address, username=user, password=pas, authMechanism=auth)

# Truy cập database 'Data_Laichau'
db = client[database]

# Truy cập collection 'LC_Meteorology'
col = db[coll_name]
# Truy vấn dữ liệu từ collection
stationid = "TU"

# Lấy dữ liệu có "Id" = "TU" và sắp xếp theo "Time" giảm dần
data_mg = col.find({"Id": stationid}).sort([("Time", -1)])

# Kiểm tra kiểu dữ liệu trả về
print(type(data_mg))
