# Định nghĩa bảng giá điện
price_table = {
    "Bậc 1": {"kwh": 0, "đơn giá": 1678},
    "Bậc 2": {"kwh": 51, "đơn giá": 1734},
    "Bậc 3": {"kwh": 101, "đơn giá": 2014},
    "Bậc 4": {"kwh": 201, "đơn giá": 2536},
    "Bậc 5": {"kwh": 301, "đơn giá": 2834},
    "Bậc 6": {"kwh": 401, "đơn giá": 2927}
}


def calculate_electricity_bill(kwh):
    total_cost = 0
    for i in range(len(price_table)):
        if kwh <= price_table[i]["kwh"]:
            total_cost += kwh * price_table[i]["đơn giá"]
            break
        else:
            kwh -= price_table[i]["kwh"]
            total_cost += price_table[i]["kwh"] * price_table[i]["đơn giá"]
    return total_cost


# Nhập số Kwh tiêu thụ
kwh = float(input("Nhập số Kwh tiêu thụ: "))

# Tính tiền điện
total_cost = calculate_electricity_bill(kwh)

# Hiển thị kết quả
print("Tổng tiền điện phải trả là:", total_cost)
