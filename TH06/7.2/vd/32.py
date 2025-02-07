import json

# Tạo dữ liệu JSON
data = {
    "Product": {
        "0": "Desktop Computer",
        "1": "Tablet",
        "2": "iPhone",
        "3": "Laptop"
    },
    "Price": {
        "0": 700,
        "1": 250,
        "2": 800,
        "3": 1200
    },
    "Manufacturer": {
        "0": "IBM",
        "1": "Apple",
        "2": "Apple",
        "3": "Dell"
    }
}

# Ghi dữ liệu vào file JSON
path_json = "data.json"
with open(path_json, 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Đọc dữ liệu từ file JSON
with open(path_json, 'r') as json_file:
    data_loaded = json.load(json_file)

# Kiểm tra kiểu dữ liệu
print("Type of loaded data:", type(data_loaded))

# Hiển thị dữ liệu
print("\nProduct List:", data_loaded['Product'])
print("\nPrice List:", data_loaded['Price'])
print("\nManufacturer List:", data_loaded)
