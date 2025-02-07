import json
import pandas as pd

# Dữ liệu JSON
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

# Tạo file JSON
path_json = "json_Data_product.json"
with open(path_json, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"File {path_json} đã được tạo thành công!")

# Đọc JSON vào DataFrame
data_json = pd.read_json(path_json)
print(data_json)
