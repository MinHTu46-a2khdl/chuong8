def sum_odd(n):
  """Tính tổng các số lẻ nhỏ hơn hoặc bằng n"""
  sum = 0
  for i in range(1, n + 1, 2):
    sum += i
  return sum

def sum_even(n):
  """Tính tổng các số chẵn nhỏ hơn hoặc bằng n"""
  sum = 0
  for i in range(2, n + 1, 2):
    sum += i
  return sum

def product(n):
  """Tính tích các số từ 1 đến n"""
  product = 1
  for i in range(1, n + 1):
    product *= i
  return product

def product_divisible_by_3(n):
  """Tính tích các số chia hết cho 3 nhỏ hơn hoặc bằng n"""
  product = 1
  for i in range(1, n + 1):
    if i % 3 == 0:
      product *= i
  return product

def sum_prime(n):
  """Tính tổng các số nguyên tố nhỏ hơn hoặc bằng n"""
  sum = 0
  for i in range(2, n + 1):
    if is_prime(i):
      sum += i
  return sum

def sum_series(n):
  """Tính tổng chuỗi đan dấu từ 1 đến n"""
  sum = 0
  for i in range(1, n + 1):
    sum += (-1)**(i - 1) / i
  return sum

def is_prime(n):
  """Kiểm tra n có phải là số nguyên tố không"""
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True


def main():
  n = int(input("Nhập vào một số nguyên n: "))

  print("A = ", sum_odd(n))
  print("B = ", sum_even(n))
  print("C = ", product(n))
  print("D = ", product_divisible_by_3(n))
  print("E = ", sum_prime(n))
  print("F = ", sum_series(n))


if __name__ == "__main__":
  main()
