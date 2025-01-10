#vd1: Tạo ma trận 0|1 kích thước m x n
import numpy as np
array_zeros = np.zeros((5,3))
print(array_zeros)
print("kieu du lieu trong mang array_zeros: ", array_zeros.dtype)
print("kich thuoc cua mang array_zeros: " , array_zeros.shape)
print("so phan tu cua mang: ", array_zeros.size)
print("so chieu cua mang: ", array_zeros.ndim)
#phuong thuc ones: tao ma tran 1 kich thuoc 3 hang x 5 cot
import numpy as np

# Create an array of ones with dtype=int
array_one = np.ones((3, 5), dtype=int)  # Changed np.int to int

# Print the array
print(array_one)

# Print information about the array
print("Kiểu dữ liệu trong mảng array_one:", array_one.dtype)
print("Kích thước của mảng array_one:", array_one.shape)
print("Số phần tử của mảng:", array_one.size)
print("Số chiều của mảng:", array_one.ndim)

#vd2: tao ma tran don vi cap n
import numpy as np
array_eye = np.eye(5)
print(array_eye)
print("Kieu du lieu cua phan tu trong mang: ", array_eye.dtype)
print("Kích thước của mảng :", array_eye.shape)
print("Số phần tử của mảng:", array_eye.size)
print("Số chiều của mảng:", array_eye.ndim)

#vd3: tao ma tran voi cac phan tu ngau nhien trong khoang(0,1)
import numpy as np
array_random = np.random.rand(7, 5)
print(array_random)
print("Kieu du lieu cua phan tu trong mang: ", array_random.dtype)
print("Kích thước của mảng :", array_random.shape)
print("Số phần tử của mảng:", array_random.size)
print("Số chiều của mảng:", array_random.ndim)

#vd4: tao vector, ma tran voi cac phan tu la so nguyen ngau nhien trong khoang(low,high)
import numpy as np

# Khoảng giá trị của số nguyên ngẫu nhiên
low = 1
high = 10

# Tạo vector có 10 phần tử ngẫu nhiên trong khoảng (low, high)
vector = np.random.randint(low, high, size=10)
print("Vector ngẫu nhiên:")
print(vector)

# Tạo ma trận 3x4 với các phần tử ngẫu nhiên trong khoảng (low, high)
matrix = np.random.randint(low, high, size=(3, 4))
print("\nMa trận ngẫu nhiên:")
print(matrix)

#vd5: tao vector voi cac tham so thiet lap
#phuong thuc arange(a,b,step)
import numpy as np
d = np.arange(1,15,2)
print('vector d: ',d)
print("so phan tu cua vevtor d : ",d.size)
print('----------------------------------------------')
#phuong thuc linspace(a,b,num)
f =np.linspace(1,15,11)
print('vector f: ',f)
print("so phan tu cua vevtor f : ",f.size)

#vd6:
import numpy as np

# Đọc dữ liệu từ file Diem_2A.txt
path = 'D:\Python\PythonGit\Diem_2A.txt'
diem_2a = np.loadtxt(path, delimiter=' ', dtype=np.int_)

print(diem_2a)
print("Kiểu dữ liệu của phần tử trong mảng diem_2a:", diem_2a.dtype)
print("Kích thước của mảng diem_2a:", diem_2a.shape)
print("Số phần tử của mảng diem_2a:", diem_2a.size)
print("Số chiều của mảng diem_2a:", diem_2a.ndim)

#VDVD28
a_float = np.linspace(0,15,11)
print(a_float)
print('Kiểu Dữ liệu: ', a_float.dtype)

a_int = a_float.astype(np.int16)
print(a_int)
print('Dữ liệu sau khi chuyển: ', a_int.dtype)
#----------
# Chuyển từ kiểu float --> int
a_str = a_int.astype(np.str)
print(a_str)
print('Dữ liệu sau khi chuyển: ', a_str.dtype)

# Chuyển từ kiểu float --> boolean
a_bol = a_int.astype(np.bool)
print(a_bol)
print('Dữ liệu sau khi chuyển:', a_bool.dtype)
#
#---------------------------------------------------
#VD31
import numpy as np

# Tạo một mảng NumPy
a = np.array([3, 5, 10, 19, 8, 1, 9, 8, 3, 1])
# In ra các phần tử của mảng
print("Các phần tử của vector 'a':\n", a)
# Truy cập phần tử đầu tiên
print("Phần tử đầu tiên:", a[0])
# Truy cập phần tử thứ 3 (vị trí index là 2)
print("Phần tử thứ 3:", a[2])
# Truy cập phần tử cuối cùng
print("Phần tử cuối cùng:", a[-1])

#-------------

# Truy cập nhiều phần tử của vector 'a'
print("Các phần tử của vector 'a':\n", a)
# 3 phần tử đầu tiên
print("3 phần tử đầu tiên:", a[:3])
# Từ phần tử thứ 5 tới hết
print("Từ phần tử thứ 5 tới hết:", a[5:])
# Từ phần tử thứ 2 đến phần tử thứ 6 (không bao gồm phần tử thứ 6)
print("Từ phần tử thứ 2 đến phần tử thứ 6 của vector:", a[2:6])
#
#---------------------------------------------------

#VD32
# Truy cập tới 1 phần tử của ma trận (2D): a[index_row, index_col]
print('Điểm môn học đầu tiên, của học sinh đầu tiên:', diem_2a[0,0])
print('Điểm môn học thứ 1, của học sinh thứ 3:', diem_2a[2,1])
print('Điểm môn cuối cùng, của học sinh cuối cùng:', diem_2a[-1,-1])
print()

print('Bảng điểm lớp 2A:\n', diem_2a)
#
#---------------------------------------------------
#VD33
# Truy cập tới nhiều phần tử trong ma trận: a[index_row1:index_row2, index_col1:index_col2]
# Lấy điểm tất cả các môn (tất cả các hàng) của học sinh 5:
diem_hs5 = diem_2a[:, 5]
print("Điểm các môn của học sinh 5:", diem_hs5)
# Lấy điểm môn học cuối cùng của tất cả học sinh (tất cả các cột)
diem_mon = diem_2a[-1, :]
print("Điểm môn học cuối cùng của tất cả học sinh: \n", diem_mon)
# Lấy điểm 5 môn học đầu tiên của 10 học sinh đầu tiên
diem5_hs10 = diem_2a[:5, :10]
print("Bảng điểm 5 môn học đầu tiên của 10 học sinh đầu của lớp: \n", diem5_hs10)
#
#---------------------------------------------------

