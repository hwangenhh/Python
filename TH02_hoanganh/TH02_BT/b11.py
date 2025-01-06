#kiem tra so nguyen to
def is_prime(n):
  """Kiểm tra xem n có phải là số nguyên tố hay không.

  Args:
    n: Số tự nhiên cần kiểm tra.

  Returns:
    True nếu n là số nguyên tố, False nếu không.
  """
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

# Nhập vào số tự nhiên N
n = int(input("Nhập vào số tự nhiên N: "))

# Kiểm tra xem N có phải là số nguyên tố hay không
if is_prime(n):
  print(f"{n} là số nguyên tố.")
else:
  print(f"{n} không phải là số nguyên tố.")