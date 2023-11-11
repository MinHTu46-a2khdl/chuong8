def e_x(x, n):
  """
  Tính giá trị gần đúng của hàm e^x với x là giá trị đầu vào

  Args:
    x: Giá trị đầu vào
    n: Số hạng của khai triển Taylor

  Returns:
    Giá trị gần đúng của hàm e^x
  """

  ans = 1
  for i in range(1, n + 1):
    ans += x**i / math.factorial(i)
  return ans


def main():
  """
  Hàm chính
  """

  x = float(input("Nhập giá trị x: "))
  n = int(input("Nhập số hạng của khai triển Taylor: "))
  ans = e_x(x, n)
  print("Giá trị gần đúng của e^x là:", ans)


if __name__ == "__main__":
  main()
