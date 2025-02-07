import pandas as pd
import requests as rq

url_api = 'http://api.exchangeratesapi.io/v1/latest?access_key=06a81a333abfe2ac294f7bc88bac1ec9'
# Lấy dữ liệu theo url_api
result_money = rq.get(url_api)
print(result_money.status_code)
# Chuyển đổi dữ liệu sang kiểu string
data_text = result_money.text
# Chuyển đổi dữ liệu sang kiểu JSON
data_json = result_money.json()
print('Text:', data_text)
print('Json:', data_json)
df = pd.DataFrame(data_json)
print(df.head(10))
