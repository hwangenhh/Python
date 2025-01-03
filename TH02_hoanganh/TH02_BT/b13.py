def decimal_to_binary(n):
  """Chuyển đổi số thập phân sang hệ nhị phân."""
  if n == 0:
    return "0"
  binary = ""
  while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n //= 2
  return binary

# Nhập vào số tự nhiên N
N = int(input("Nhập vào số tự nhiên N (N>0): "))

# Chuyển đổi N sang hệ nhị phân
binary_N = decimal_to_binary(N)

# In ra kết quả
print(f"Số {N} trong hệ nhị phân là: {binary_N}")