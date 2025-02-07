import pandas as pd

# Đọc toàn bộ file Excel và lấy danh sách các sheet
file_path = r"D:\PHYTHON\7.2\bt\excel_Data_Movies.xls"  # Đường dẫn chính xác
sheets = pd.read_excel(file_path, sheet_name=None)  # Đọc tất cả sheet

# Duyệt qua từng sheet và hiển thị dữ liệu
for sheet_name, df in sheets.items():
    print(f"📄 Sheet: {sheet_name}")
    print(df.head())  # Hiển thị 5 dòng đầu của từng sheet
    print("\n")
