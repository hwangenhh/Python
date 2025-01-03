def is_prime(n):
  """Kiểm tra xem một số có phải là số nguyên tố hay không."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def prime_numbers(n):
  """Hiển thị các số nguyên tố từ 2 tới N."""
  print("Các số nguyên tố từ 2 tới", n, "là:")
  for i in range(2, n + 1):
    if is_prime(i):
      print(i, end=" ")

# Nhập số N
n = int(input("Nhập vào một số N: "))

# Hiển thị các số nguyên tố từ 2 tới N
prime_numbers(n)