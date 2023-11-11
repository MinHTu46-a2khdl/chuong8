def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            x = "Vô số nghiệm"
        else:
            x = "Vô nghiệm"
    else:
        x = -b / a
    return x


a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

x = solve_linear_equation(a, b)

print("Nghiệm của phương trình là:", x)
