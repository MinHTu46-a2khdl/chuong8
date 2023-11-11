def calculate_expression(x, n):
  """
  Tính toán biểu thức (x² + x + 1)^n + (x² - x + 1)^n

  Args:
    x: Số thực
    n: Số mũ

  Returns:
    Kết quả của biểu thức
  """

  # Tính toán (x² + x + 1)^n
  a = x**2 + x + 1
  b = a**n

  # Tính toán (x² - x + 1)^n
  c = x**2 - x + 1
  d = c**n

  # Trả về kết quả
  return b + d

if __name__ == "__main__":
  # Nhập x và n
  x = float(input("Nhập x: "))
  n = int(input("Nhập n: "))

  # Tính toán biểu thức
  A = calculate_expression(x, n)

  # In kết quả
  print("A = (x² + x + 1)^n + (x² - x + 1)^n = %f" % A)
