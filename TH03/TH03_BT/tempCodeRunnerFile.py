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
