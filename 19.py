def main():
  input_number = int(input("Nhập số: "))
  output_list = []
  for i in range(input_number, 0, -2):
    output_list.append(i)
  print(output_list)

if __name__ == "__main__":
  main()
