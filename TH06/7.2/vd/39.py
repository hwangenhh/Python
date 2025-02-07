import pandas as pd
import requests as rq

# Đường dẫn API với access_key
url_api = 'http://api.exchangeratesapi.io/v1/latest?access_key=06a81a333abfe2ac294f7bc88bac1ec9'

# Các loại tiền tệ cần lấy tỷ giá
symbols = 'USD, JPY, THB, VND, MYR, GBP, KRW'

# Gửi yêu cầu GET tới API
result_money1 = rq.get(url_api, params={'symbols': symbols})

# Kiểm tra xem request có thành công không
if result_money1.status_code == 200:
    # Chuyển dữ liệu JSON thành dictionary
    data_json1 = result_money1.json()
    
    # Lấy phần "rates" từ JSON
    rates = data_json1.get("rates", {})

    # Chuyển đổi rates thành DataFrame
    df1 = pd.DataFrame(rates.items(), columns=["Currency", "Exchange Rate"])

    # Hiển thị dữ liệu
    print(df1.head(10))
else:
    print(f"Lỗi khi lấy dữ liệu từ API: {result_money1.status_code}")
