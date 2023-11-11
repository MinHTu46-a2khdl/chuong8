def find_max_min_by_minmax(a, b, c, d):
    max_num = max(a, b, c, d)
    min_num = min(a, b, c, d)

    return max_num, min_num


a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d = int(input("Nhập số d: "))

max_num, min_num = find_max_min_by_minmax(a, b, c, d)

print("Số lớn nhất là:", max_num)
print("Số nhỏ nhất là:", min_num)
