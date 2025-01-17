import numpy as np

# Define the vector
vector_a = np.array([5, 7, 2, 9, 10, 15, 2, 9, 2, 17, 28, 16], dtype=np.int16)
print("Vector a:")
print(vector_a)
print("Number of elements in vector: ", vector_a.size)
print("---------------")

# Reshape vector to matrix (3 x 4)
matrix_a = vector_a.reshape((3, 4))
print("Reshape to matrix: 3 x 4")
print(matrix_a)
print("Number of elements in matrix_a: ", matrix_a.size)
print("----------")

# Reshape vector to matrix (2 x 6)
matrix_b = vector_a.reshape((2, 6))
print("Reshape to matrix: 2 x 6")
print(matrix_b)
print("Number of elements in matrix_b: ", matrix_b.size)

# Example 2: Convert matrix to vector
a1_2d = np.array([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])
print('Matrix: \n', a1_2d)
print("---------------")
print('a) Ravel by row (default order=\'C\')')
print(a1_2d.ravel())
print('\nb) Ravel by column (order=\'F\')')
print(a1_2d.ravel(order='F'))

# Example 3: Split vector
# Example from page 9
x = np.arange(0, 6)
print(x)
# Split vector into 2 vectors
x1, x2 = np.split(x, 2)
print(x1, x2)

# Another example of splitting
x = np.arange(1, 10)
print(x)
x1, x2, x3 = np.split(x, [2, 6])  # Splits at indices 2 and 6
print(x1, x2, x3)

# Example 4: Flip a matrix
# Define matrix A
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Flip matrix by columns
A1 = np.flip(A, 1)  # Equivalent to np.fliplr(A)
print('Flip matrix by columns: \n', A1)

# Flip matrix by rows
A2 = np.flip(A, 0)  # Equivalent to np.flipud(A)
print('Flip matrix by rows: \n', A2)

#vd trang 16
import numpy as np
x = np.arange(8)
print("x = ", x)
print('----------------------')
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("-x = ", -x)
print("x * 2 = ", x * 2)
print("x / 2 = ", x / 2)
print("x // 2 = ", x // 2)
print("x % 2 = ", x % 2)
print("x ^ 3 = ", x ** 3)
print("x = ", x)
print('------------------')
print("x + 5 =  ", np.add(x,5))
print("x - 5 =  ", np.subtract(x,5))
print("-x =  ", np.negative(x))
print("x * 2 =  ", np.multiply(x,2))
print("x / 2 =  ", np.divide(x,2))
print("x // 2 = ", np.floor_divide(x,2))
print("x % 2 = ", np.mod(x,2))
print("x ^ 3 = ", np.power(x,3))

#vd trang 17
import numpy as np
x = np.array([-2, -1, 0, 1, 2])
print("x =   ",x)
print('--------------')
print(np.abs(x))  
print(np.absolute(x))  

#vd trng 19
import numpy as np
x = np.array([1,2,3])
print(x)
print('----------------')
print("e^x = ", np.exp(x))
print("2^x = ", np.exp2(x))
print("3^x = ", np.power(3,x))

x=np.array([1,2,4,100])
print("x = ", x)
print('----------------')
print("ln(x) =  ",np.log(x))
print("log2(x) = ", np.log2(x))
print("log10(x) = ", np.log10(x))

#vd trang 20
import numpy as np
arr = np.array([20.8999,67.89899,54.43409])
print(arr)
print('----------------')
#1)Lam tron toi so 2 sau dau,
print(np.around(arr,1))
#2)Lam tron toi so 2 sau dau,
print(np.around(arr,2))
#3) lam tron xuong so nguyen gan nhat
print(np.floor(arr))
#4)lam tron len so nguyen gan nhat
print(np.ceil(arr))

#vd trang 23
import numpy as np
a = np.random.randint(1,33,15)
print("Vector ban dau : \n ", a)
print('-----------------')
#sap xep vector a tang dan
a_sort = np.sort(a)
#sap xep vector a giam dan:
#1) Lat vector a_sort e sap xep giam dan
b_sort = np.flip(a_sort)
#2) Su dung -np.sort(-x)
b_sort = -np.sort(-a)
print('Vector sap xep tang dan: \n', a_sort)
print('Vector sap xep giam dan: \n', b_sort)

#vd trang 28
import numpy as np
x = np.array([17,2,11,1,9,15,1,3,8,1,12,13,5])
#1) tim kiem cac phan tu co gia tri ==1
t1 = np.where(x==1)
print(t1)
print('1. so phan tu thoa man dieu kien = 1: ', t1[0].size)
print('--------------')
#2) tim kiem cac phan tu co gia tri > 10
t2 = np.where(x>10)
print(t2)
print('2.So phan tu thoa man dieu kien > 10: ', t2[0].size)
print('--------------')
#3) tim kiem cac phan tu co gia tri [5,12)
t3 = np.where((x>=5) & (x<12))
print(t3)
print('3.So phan tu thoa man dieu kien [5,10): ', t3[0].size)

#vd trang 29
import numpy as np

# Define the matrix
arr = np.array([(1, 2, 3, 4, 5, 4, 4), (7, 3, 4, 8, 9, 6, 7)])

# Find elements greater than 4
x = np.where(arr > 4)

print('Matrix A: \n', arr)
print('--------------')
print('Indices of elements greater than 4: ', x)
print('Number of elements that satisfy the condition (> 4): ', x[0].size)



