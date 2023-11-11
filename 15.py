def gcd(a, b):
  """Tìm ước chung lớn nhất của 2 số a và b"""
  while b != 0:
    a, b = b, a % b
  return a


def main():
  a = int(input("Nhập vào số a: "))
  b = int(input("Nhập vào số b: "))

  print("Ước chung lớn nhất của a và b là:", gcd(a, b))


if __name__ == "__main__":
  main()
