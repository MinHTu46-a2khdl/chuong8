def sum_numbers(numbers):
  """Tính tổng các số nguyên trong danh sách numbers"""
  sum = 0
  for number in numbers:
    if number != 0:
      sum += number
  return sum


def main():
  numbers = list(map(int, input("Nhập vào các số nguyên cách nhau bằng dấu cách: ").split()))

  # Bỏ hết các phần tử sau số 0
  numbers = [number for number in numbers if number != 0]

  print("Tổng các số nguyên là:", sum_numbers(numbers))


if __name__ == "__main__":
  main()
