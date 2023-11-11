def gcd(a, b):
  """Tìm ước số chung lớn nhất của a và b"""
  while b:
    a, b = b, a % b
  return a


def lcm(a, b):
  """Tìm bội chung nhỏ nhất của a và b"""
  return a * b // gcd(a, b)


def main():
  a, b = map(int, input("Nhập vào 2 số nguyên a và b: ").split())

  print("Bội chung nhỏ nhất của a và b là:", lcm(a, b))


if __name__ == "__main__":
  main()
