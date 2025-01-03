chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

bmi = can_nang / (chieu_cao * chieu_cao)

print(f"Chỉ số BMI của bạn là: {bmi:.2f}")

if bmi < 18.5:
  print("Bạn đang thiếu cân.")
elif bmi < 25:
  print("Bạn đang ở mức cân nặng khỏe mạnh.")
elif bmi < 30:
  print("Bạn đang thừa cân.")
else:
  print("Bạn đang béo phì.")