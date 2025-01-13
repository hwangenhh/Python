import numpy as np

# Đọc dữ liệu từ file Temp.txt vào data_numpy
data_numpy = np.loadtxt('Temp.txt')

# Hiển thị các thông tin của biến data_numpy
print("Kích thước của mảng (shape):", data_numpy.shape)
print("Số chiều của mảng (ndim):", data_numpy.ndim)
print("Kiểu dữ liệu của mảng (dtype):", data_numpy.dtype)
print("Số phần tử trong mảng (size):", data_numpy.size)
