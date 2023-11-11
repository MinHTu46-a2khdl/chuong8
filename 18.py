def is_perfect(n):
  """Kiểm tra n có phải là số hoàn hảo không"""
  sum = 0
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      sum += i
      sum += n // i
  return sum == n


def main():
  n = int(input("Nhập vào một số nguyên n: "))

  if is_perfect(n):
    print(n, "là số hoàn hảo")
  else:
    print(n, "không phải là số hoàn hảo")


if __name__ == "__main__":
  main()
