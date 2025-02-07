import pandas as pd

# Đường dẫn đến file Excel
path_excel = "data-demo1.xlsx"  # Đảm bảo file có đúng định dạng .xlsx

# Đọc dữ liệu từ sheet 3 ['4080130_03'], không có dòng header
data_ex33 = pd.read_excel(path_excel, 
                         sheet_name='4080130_02', 
                         header=None)  # Không lấy dòng đầu làm tiêu đề

# Hiển thị thông tin về DataFrame
data_ex33.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex33.head()
