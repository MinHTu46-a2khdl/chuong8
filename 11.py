def is_prime(n):
  """
  Kiểm tra xem n có phải là số nguyên tố hay không

  Args:
    n: Số nguyên cần kiểm tra

  Returns:
    True nếu n là số nguyên tố, False nếu ngược lại
  """

  # Kiểm tra xem n có bằng 1 hay không
  if n == 1:
    return False

  # Tính căn bậc hai của n
  sqrt_n = int(n ** 0.5)

  # Kiểm tra xem n có chia hết cho bất kỳ số nguyên nào nhỏ hơn hoặc bằng sqrt_n hay không
  for i in range(2, sqrt_n + 1):
    if n % i == 0:
      return False

  # Kết luận
  return True

if __name__ == "__main__":
  n = int(input("Nhập n: "))
  if is_prime(n):
    print("n là số nguyên tố")
  else:
    print("n không phải là số nguyên tố")
