import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu về diện tích và giá bán nhà (1)
square_feet = np.array([1460, 2108, 1743, 1499, 1864, 2391, 1977, 1610, 1530, 1759, 1821, 2216])  # Diện tích
prices_1 = np.array([288700, 309300, 301400, 291100, 302400, 314900, 305400, 297000, 292400, 298200, 304300, 311700])  # Giá bán

# Dữ liệu về khoảng cách từ trung tâm thành phố và giá bán nhà (2)
distance = np.array([2.6, 0.8, 1.0, 0.6, 1.5, 2.0, 3.4, 1.2, 3.6, 1.7])
prices_2 = np.array([214000, 376000, 280000, 362000, 200000, 190000, 236000, 244000, 128000, 165000])

# Tính hệ số tương quan (correlation coefficient) cho diện tích và giá bán nhà
a = np.corrcoef(square_feet, prices_1)[0, 1]

# Tính hệ số tương quan (correlation coefficient) cho khoảng cách từ trung tâm thành phố và giá bán nhà
b = np.corrcoef(distance, prices_2)[0, 1]

# In kết quả
print("Hệ số tương quan giữa diện tích và giá bán nhà:", a)
print("Hệ số tương quan giữa khoảng cách từ trung tâm và giá bán nhà:", b)

# Vẽ biểu đồ để minh họa
plt.figure(figsize=(12, 6))

# Biểu đồ 1: Diện tích vs Giá bán nhà
plt.subplot(1, 2, 1)
plt.scatter(square_feet, prices_1, color='blue')
plt.title("Diện tích vs Giá bán nhà")
plt.xlabel("Diện tích (Square Feet)")
plt.ylabel("Giá bán (USD)")

# Biểu đồ 2: Khoảng cách vs Giá bán nhà
plt.subplot(1, 2, 2)
plt.scatter(distance, prices_2, color='green')
plt.title("Khoảng cách từ trung tâm vs Giá bán nhà")
plt.xlabel("Khoảng cách (Miles)")
plt.ylabel("Giá bán (USD)")

plt.tight_layout()
plt.show()
