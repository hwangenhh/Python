# Đọc tập dữ liệu Boston House Prices Dataset
import sklearn.datasets as datask

# Tải dữ liệu, return_X_y=True để nhận cả features (X) và target (y)
X, y = datask.load_boston(return_X_y=True)

print(type(X))  # Kiểu dữ liệu của X
print("Kích thước dữ liệu đầu vào (features):", X.shape)
print("Kích thước dữ liệu đầu ra (target):", y.shape)
