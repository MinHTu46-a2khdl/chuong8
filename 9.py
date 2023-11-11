def calculate_s(x, n):
  """
  Tính toán giá trị của s theo công thức s = (x^2 + 1)^n

  Args:
    x: Số thực
    n: Số nguyên dương

  Returns:
    Giá trị của s
  """

  if not isinstance(x, (float, complex)):
    raise TypeError("x phải là số thực hoặc số phức")
  if not isinstance(n, int) or n < 0:
    raise TypeError("n phải là số nguyên dương")

  return (x ** 2 + 1) ** n


if __name__ == "__main__":
  x = float(input("Nhập x: "))
  n = int(input("Nhập n: "))

  s = calculate_s(x, n)
  print(f"s = {s}")
