import numpy as np

# Đọc dữ liệu từ file CSV
data = np.loadtxt('Temp.txt')

# Yêu cầu 2: Tính Max, Min, và nhiệt độ trung bình cho cả 6 thành phố
overall_max = data.max()
overall_min = data.min()
overall_mean = data.mean()

print("Yêu cầu 2:")
print(f"Nhiệt độ cao nhất (Max) của cả 6 thành phố: {overall_max:.2f}°C")
print(f"Nhiệt độ thấp nhất (Min) của cả 6 thành phố: {overall_min:.2f}°C")
print(f"Nhiệt độ trung bình của cả 6 thành phố: {overall_mean:.2f}°C")

# Yêu cầu 3: Tính Max, Min, và nhiệt độ trung bình cho từng thành phố
# Assuming each row corresponds to a different city
city_max = data.max(axis=0)
city_min = data.min(axis=0)
city_mean = data.mean(axis=0)

listTP = ["Hà Nội", "Vinh", "Đà Nẵng", "Nha Trang", "Hồ Chí Minh", "Cà Mau"]

# In kết quả cho từng thành phố
print("\nYêu cầu 3:")
print("Nhiệt độ cao nhất (Max), thấp nhất (Min), và trung bình (Mean) của từng thành phố:")
for i,a in enumerate(listTP):
    print(f"Thành phố {a}: Max = {city_max[i]:.2f}°C, Min = {city_min[i]:.2f}°C, Mean = {city_mean[i]:.2f}°C")

# Yêu cầu 4
data_thongke = np.vstack([np.append(city_max, overall_max), 
                          np.append(city_mean, overall_mean), 
                          np.append(city_min, overall_min)])

# Save the result to a file (thongke.txt) with UTF-8 encoding
header = "Hà Nội,Vinh,Đà Nẵng,Nha Trang,Hồ Chí Minh,Cà Mau,Overall"
np.savetxt('thongke.txt', data_thongke.T, delimiter=',', header=header, comments='', fmt="%.2f", encoding='utf-8')

# Print the result for verification
print("\nYêu cầu 4: Kết quả thống kê nhiệt độ")
for i, city in enumerate(listTP):
    print(f"Thành phố {city}: Max = {data_thongke[0,i]:.2f}°C, Mean = {data_thongke[1,i]:.2f}°C, Min = {data_thongke[2,i]:.2f}°C")

print(f"\nThống kê chung cho cả 6 thành phố:")
print(f"Max chung = {data_thongke[0,-1]:.2f}°C, Mean chung = {data_thongke[1,-1]:.2f}°C, Min chung = {data_thongke[2,-1]:.2f}°C")