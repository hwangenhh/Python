import numpy as np
#Trang 13
a = np.array([1, 2, 5, 7, 0, 8])

print(a)
print("Loại dữ liệu của biến a:", type(a))
print("Kiểu dữ liệu của phần tử trong mảng a:", a.dtype)
print("Kích thước của mảng a:", a.shape)
print("Số phần tử của mảng a:", a.size)
print("Số chiều của mảng a:", a.ndim)

#14
# Tạo mảng 2 chiều (2D - Ma trận)
b = np.array([(4, 5, 6.0), (1, 2, 3.5)])

print(b)
print("Loại dữ liệu của biến b:", type(b))
print("Kiểu dữ liệu của phần tử trong mảng b:", b.dtype)
print("Kích thước của mảng b:", b.shape)
print("Số phần tử của mảng b:", b.size)
print("Số chiều của mảng b:", b.ndim)

#15
c = np.array([[(2,4,0,6), (4,7,5,6)],
              [(0,3,2,1), (9,4,5,6)],
              [(5,8,6,4), (1,4,6,8)]]) # mảng 3 chiều (3D)

print(c)
print("Phần tử đầu tiên của mảng c:", c[0,0,0])
print("Kiểu dữ liệu của phần tử trong mảng c:", c.dtype)
print("Kích thước của mảng c:", c.shape)
print("Số phần tử của mảng c:", c.size)
print("Số chiều của mảng c:", c.ndim)

#18
array_zeros = np.zeros((5, 3))

print(array_zeros)
print("Kiểu dữ liệu trong mảng array_zeros:", array_zeros.dtype)
print("Kích thước của mảng array_zeros:", array_zeros.shape)
print("Số phần tử của mảng array_zeros:", array_zeros.size)
print("Số chiều của mảng array_zeros:", array_zeros.ndim)

#19
array_eye = np.eye(5)

print(array_eye)
print("Kiểu dữ liệu của phần tử trong mảng array_eye:", array_eye.dtype)
print("Kích thước của mảng array_eye:", array_eye.shape)
print("Số phần tử của mảng array_eye:", array_eye.size)

#20
array_random = np.random.random((7, 5))

print(array_random)
print("Kiểu dữ liệu của phần tử trong mảng array_random:", array_random.dtype)
print("Kích thước của mảng array_random:", array_random.shape)
print("Số phần tử của mảng array_random:", array_random.size)
print("Số chiều của mảng array_random:", array_random.ndim)
#21
# Tạo một vector ngẫu nhiên có 5 phần tử trong khoảng (low, high)
low = 1
high = 10
vector = np.random.randint(low, high, size=5)
print("Vector:")
print(vector)

# Tạo một ma trận ngẫu nhiên 3x3 trong khoảng (low, high)
matrix = np.random.randint(low, high, size=(3, 3))
print("\nMatrix:")
print(matrix)

#22
# Phương thức arange(a, b, steps):
# Tạo vector:
# Phần tử đầu tiên = a,
# kết thúc < b,
# mỗi phần tử cách nhau một khoảng = steps
d = np.arange(1, 15, 2)
print('Vector d:', d)
print('Số phần tử của vector d:', d.size)

print()

# Phương thức linspace(a, b, num)
# Tạo vector:
# Phần tử đầu tiên = a,
# Phần tử kết thúc = b,
# Số phần tử của ma trận = num
f = np.linspace(1, 15, 11)
print('Vector f:', f)
print('Số phần tử của vector f:', f.size)

#25
# Đọc dữ liệu từ file Diem_2A.txt
path = 'Data_Exercise/Diem_2A.txt'
diem_2a = np.loadtxt(path, delimiter=',', dtype=np.int)

print(diem_2a)
print("Kiểu dữ liệu của phần tử trong mảng diem_2a:", diem_2a.dtype)
print("Kích thước của mảng diem_2a:", diem_2a.shape)
print("Số phần tử của mảng diem_2a:", diem_2a.size)
print("Số chiều của mảng diem_2a:", diem_2a.ndim)

#40
print('Điểm cao nhất của lớp:',diem_2a.max())
print('Điểm thấp nhất của lớp:', diem_2a.min())

for i in range(0,diem_2a.shape[0]):
    print('Môn', i,': Điểm Max:', diem_2a[i,:].max(),' - Điểm Min:',diem_2a[i,:].min())

for i in range(0,diem_2a.shape[1]):
    print('Học sinh', i,': Điểm Max:', diem_2a[:,i].max(),'-- Điểm Min:', diem_2a[:,i].min())

#41
#Sum: Tính tổng các phần tử trong mảng

print('Tổng tất cả các điểm trong của lớp 2A:', diem_2a.sum())
print('--------------------------------')

#Tính tổng điểm của từng học sinh:

for i in range(0,diem_2a.shape[1]):
    print('Tổng điểm các môn của học sinh', i,':', diem_2a[:,i].sum())

#43
print('Điểm trung bình của cả lớp 2A:', diem_2a.mean())
print('--------------------------------')
#Tính điểm trung bình của các học sinh trong lớp:
#CÁCH 1:
for i in range(0,diem_2a.shape[1]):
    print('Điểm trung bình của học sinh', i,':', diem_2a[:,i].mean())

#CÁCH 2:
mean_2a = diem_2a.mean(axis=0)
#axis = 0: theo hàng
#axis = 1: theo cột
for i in range(0,mean_2a.size):
    print('Điểm trung bình của học sinh', i,':', mean_2a[i])

#44
#median(): Giá trị trung vị trong một tập hợp các phần tử.
#Trường hợp số phần tử trong mảng là lẻ

a=diem_2a[1,:15]

print('Mảng a ban đầu: \n', a)
print('Số phần tử trong mảng a:', a.size)
print('Mảng a đã sắp xếp: \n', np.sort(a))
print('Giá trị trung bình mean:', np.mean(a))
print('Giá trị trung vị median:', np.median(a))

#45
#C) Mode: Là giá trị xuất hiện nhiều nhất trong tập hợp.
#Trong trường hợp không có giá trị nào được lặp lại thì không có Mode.
#Liệt kê điểm xuất hiện nhiều nhất theo từng môn học

from scipy import stats as sp #sử dụng thư viện scipy để dùng hàm mode

for i in range(0,diem_2a.shape[0]):
    a = sp.mode(diem_2a[i,:])
    print('Môn', i, ': Điểm xuất hiện nhiều nhất: ', a[0], 'số lần: ', a[1])

print(type(a))

#46
#C) Mode: Là giá trị xuất hiện nhiều nhất trong tập hợp.
#Trong trường hợp không có giá trị nào được lặp lại thì không có Mode.
#Liệt kê điểm xuất hiện nhiều nhất theo từng môn học

from scipy import stats as sp #sử dụng thư viện scipy để dùng hàm mode

for i in range(0,diem_2a.shape[0]):
    a = sp.mode(diem_2a[i,:])
    print('Môn', i, ': Điểm xuất hiện nhiều nhất: ', a[0],
    'số lần: ', a[1])

print(type(a))

#47
#E) Std: Tính độ lệch chuẩn

a = np.array([10,1,1,9,12,1,9,12,10])
print('Phần tử của mảng a:',a)
print('Giá trị trung bình:',a.mean())
print('Độ lệch chuẩn:', a.std())

print('--------------------------------')

b = np.array([7,7,8,7,8,7,7,7,7])
print('Phần tử của mảng b:',b)
print('Giá trị trung bình:',b.mean())
print('Độ lệch chuẩn:', b.std())

#53
#corrcoef: Hệ số tương quan
#Thời gian dành cho học bài
a_giohoc = np.array([4,7,1,2,8,0,3,8,6])
#Điểm thi nhận được:
b_diem = np.array([7,9,3,4,9,0,5,10,8])
co = np.corrcoef(a_giohoc, b_diem)
print(type(co))
print('Hệ số tương quan: \n', co) 

