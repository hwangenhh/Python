def in_bang_cuu_chuong(n):
  """In bảng cửu chương cho số n.

  Args:
    n: Số cần in bảng cửu chương.

  Returns:
    None.
  """
  if 1 <= n <= 10:
    for i in range(1, 11):
      print(f"{n} x {i} = {n * i}")
  else:
    print("Vui lòng nhập số từ 1 đến 10.")

# Nhập số cần in bảng cửu chương
n = int(input("Nhập vào bảng cửu chương muốn in (1-10): "))

# In bảng cửu chương
in_bang_cuu_chuong(n)