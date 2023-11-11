def sum_numbers(numbers):
  """Tính tổng các số nguyên trong danh sách numbers"""
  sum = 0
  for number in numbers:
    sum += number
  return sum


def main():
  numbers = list(map(int, input("Nhập vào một dãy số nguyên cách nhau bởi dấu cách: ").split()))

  print("Tổng các số nguyên trong dãy là: ", sum_numbers(numbers))


if __name__ == "__main__":
  main()
