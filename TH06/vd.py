#vd trang11
import pandas as pd
path = 'd:\Python\PythonGit\Data_CSV.csv'
data = pd.read_csv(path)
data.info()

#vd trang 13
data1 = pd.read_csv(path, index_col = 0)
data1.info()

#vd trang 14
data2 = pd.read_csv(path,nrows=100, usecols=['chieo cao_cm','can nang_kg'])
data2.info()

#vd trang 15
data3 = pd.read_csv(path, names=['ID', 'Sex','H(cm)','W(kg)'], skiprows=5)
data3.info()

#vd trang 21
import pandas as pd
path_excel = 'd:\Python\PythonGit\Data_Excel.xlsx'
data_ex = pd.read_excel(path_excel)
data_ex.info()

#vd trang 23
data_ex1 = pd.read_excel(path_excel, sheet_name = 0, usecols=[1,4,5],index_col=0)
data_ex1.info()

#vd trang 24
# Đọc dữ liệu từ sheet 3 ['4080130_03'], không có dòng header
data_ex33 = pd.read_excel(path_excel, 
                         sheet_name='4080130_02', 
                         header=None)  # Không lấy dòng đầu làm tiêu đề

# Hiển thị thông tin về DataFrame
data_ex33.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex33.head()

#vd trang 25
# Đọc dữ liệu từ sheet 3 ['4080130_03'], không có dòng header
data_ex4 = pd.read_excel(path_excel, 
                         sheet_name='4080130_03', 
                         header=None)  # Không lấy dòng đầu làm tiêu đề

# Hiển thị thông tin về DataFrame
data_ex4.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex4.head()

#vd trang 26
# Tạo DataFrame giống với dữ liệu trong hình
data = {
    'Mã SV': [1621050041, 1621050262, 1621050083, 1621050131, 1621050384],
    'A': [6.7, 6.7, 7.3, 5.7, 7.0],
    'B1': [9.0, 7.0, 8.5, 5.0, 8.0],
    'B2': [5.5, 9.5, 9.0, 10.0, 9.5],
    'C1': [8.5, 8.0, 10.0, 9.0, 10.0],
    'C2': [8.0, 6.0, 9.0, 5.0, 9.0]
}

# Chuyển 'Mã SV' thành index
df = pd.DataFrame(data).set_index('Mã SV')

# Hiển thị DataFrame
print(df)