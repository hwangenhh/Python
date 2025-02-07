import sklearn.datasets as datask

# Đọc tập dữ liệu Iris với return_X_y=True
X_iris, y_iris = datask.load_iris(return_X_y=True)

# Kiểm tra kiểu dữ liệu
print(type(X_iris))

# In kích thước dữ liệu
print("Kích thước dữ liệu đầu vào (features):", X_iris.shape)
print("Kích thước dữ liệu đầu ra (target):", y_iris.shape)

# Hiển thị một số mẫu dữ liệu
print("Bộ dữ liệu 1:", X_iris[5], " -> ", y_iris[5])
print("Bộ dữ liệu 2:", X_iris[111], " -> ", y_iris[111])
