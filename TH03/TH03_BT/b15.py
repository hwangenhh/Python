#Bài 15_a: Viết hàm cho các bài đã thực hiện 
# 1) Viết hàm greeting(): Trả về câu chào với tham số truyền vào là chuỗi họ tên và năm sinh (Xem 
# lại bài tập số 2) 
def greeting(name:str, birth_year: int):
    current_year = 2025  # Bạn có thể thay đổi năm hiện tại nếu cần
    age = current_year - birth_year
    return f"Chào {name}, bạn hiện tại {age} tuổi."
# Ví dụ sử dụng các hàm
if __name__ == "__main__":
    name = input("Vui long nhap ten: ")
    age = int(input("vui long nhap nam sinh: "))
    # Ví dụ cho hàm greeting
    print(greeting(name, age))
# 2) Viết hàm rabbit_count(): tính số thỏ trong rừng khi truyền vào số tháng (Xem lại bài tập số 3) 
# 3) Viết hàm count_mark(): trả về số sinh viên học lại và tổng số sinh viên trong lớp với tham số 
# truyền vào là một danh sách bảng điểm (Xem lại bài tập số 5 ý 1, 2) 
# 17 
# Bài 15_b: Viết hàm cho các bài đã thực hiện 
# 4) Viết hàm bmi_show(): Trả về nhận xét dựa vào chỉ số BMI đã tính với 2 tham số truyền vào là chiều 
# cao, cân nặng (Xem lại bài tập số 7) 
# 5) Viết hàm cal_point(): Trả về điểm trung bình hệ 10 và hệ 4 của một học sinh khi truyền vào danh sách 
# điểm (Xem lại bài tập số 10 ý 2) 
# 6) Viết hàm list_prime(): trả danh sách các số nguyên tố trong khoảng tử 1 đến n với tham số truyền 
# vào là n (Xem lại bài tập số 12)



#2
def rabbit_count(months):
    if months < 0:
        return "Số tháng không hợp lệ."
    elif months == 0:
        return 1  # Giả sử bắt đầu với 1 cặp thỏ
    else:
        # Số lượng thỏ ban đầu
        initial_rabbits = 2
        # Tính số lượng thỏ sau x tháng
        # Số lượng thỏ tăng gấp đôi mỗi tháng
        total_rabbits = initial_rabbits * (2 ** months)
        return total_rabbits
# Nhập vào số tháng
months = int(input("Nhập vào số tháng x: "))
 # Ví dụ cho hàm rabbit_count
print(rabbit_count(months)) 

#3
def count_mark(grades):
    total_students = len(grades)
    students_failed = sum(1 for grade in grades if grade < 5)  # Giả sử điểm dưới 5 là học lại
    return students_failed, total_students



   

    # Ví dụ cho hàm count_mark
    grades = [6, 4, 7, 3, 5, 8]  # Danh sách điểm
    failed, total = count_mark(grades)
    print(f"Số sinh viên học lại: {failed}, Tổng số sinh viên: {total}")

    def bmi_show(height, weight):
    # Tính chỉ số BMI
    bmi = weight / (height ** 2)
    
    # Nhận xét dựa vào chỉ số BMI
    if bmi < 18.5:
        return f"BMI của bạn là {bmi:.2f}. Bạn đang thiếu cân."
    elif 18.5 <= bmi < 24.9:
        return f"BMI của bạn là {bmi:.2f}. Bạn có cân nặng bình thường."
    elif 25 <= bmi < 29.9:
        return f"BMI của bạn là {bmi:.2f}. Bạn đang thừa cân."
    else:
        return f"BMI của bạn là {bmi:.2f}. Bạn bị béo phì."

#4
def cal_point(grades):
    # Tính điểm trung bình hệ 10
    avg_10 = sum(grades) / len(grades)
    
    # Tính điểm trung bình hệ 4
    avg_4 = (avg_10 / 10) * 4
    
    return avg_10, avg_4

#5
def list_prime(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Ví dụ sử dụng các hàm
if __name__ == "__main__":
    # Ví dụ cho hàm bmi_show
    print(bmi_show(1.75, 68))  # Chiều cao 1.75m, cân nặng 68kg

    # Ví dụ cho hàm cal_point
    grades = [8, 7.5, 9, 6.5, 7]  # Danh sách điểm
    avg_10, avg_4 = cal_point(grades)
    print(f"Điểm trung bình hệ 10: {avg_10:.2f}, Điểm trung bình hệ 4: {avg_4:.2f}")

    # Ví dụ cho hàm list_prime
    n = 20
    primes = list_prime(n)
    print(f"Các số nguyên tố từ 1 đến {n}: {primes}")
    
# Bài 16: Xây dựng lớp Person 
# Xây dựng lớp Person: 
# • Gồm 4 Thuộc tính: – họ tên (name), năm sinh (year), chiều cao (height), cân nặng (weight) – Giá trị mặc định của các thuộc tính là thông tin của bạn 
# • Gồm 2 Phương thức: – Geeting(): Hiển thị thông tin của Person – Bmi(): Tính toán chỉ số BMI của Person
class Person:
    def __init__(self, name, year, height, weight):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight

    def greeting(self):
        current_year = 2025  # Bạn có thể thay đổi năm hiện tại nếu cần
        age = current_year - self.year
        return f"Chào {self.name}, bạn hiện tại {age} tuổi, chiều cao {self.height}m, cân nặng {self.weight}kg."

    def bmi(self):
        # Tính chỉ số BMI
        bmi_value = self.weight / (self.height ** 2)
        return f"Chỉ số BMI của {self.name} là {bmi_value:.2f}."
name = input("Vui long nhap ten: ")
year = input ("Nhap nam sinh: ")
height = input ("Nhap chieu cao: ")
weight = input ("Nhap can nang: ")
# Ví dụ sử dụng lớp Person
if __name__ == "__main__":
    person = Person()  # Tạo đối tượng Person với thông tin mặc định
    print(person.greeting())  # Hiển thị thông tin
    print(person.bmi())  # Tính toán chỉ số BMI
