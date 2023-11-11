# Định nghĩa bảng giá phòng
price_table = {
    1: 1260000,
    2: 1830000,
    3: 1830000,
    4: 2120000,
    5: 2120000,
    6: 2540000,
    7: 4800000,
    8: 4800000
}


def calculate_room_fee(room_type, num_of_nights):
    total_fee = 0
    if num_of_nights <= 1:
        total_fee = price_table[room_type] * num_of_nights
    else:
        if num_of_nights <= 3:
            discount_rate = 0.25
        else:
            discount_rate = 0.3
        for i in range(1, num_of_nights + 1):
            price = price_table[room_type] * (1 - discount_rate)
            total_fee += price
    return total_fee


# Nhập loại phòng và số đêm thuê
room_type = int(input("Nhập loại phòng (1-8): "))
num_of_nights = int(input("Nhập số đêm thuê: "))

# Tính tiền thuê phòng
total_fee = calculate_room_fee(room_type, num_of_nights)

# Hiển thị kết quả
print("Tổng tiền thuê phòng là:", total_fee)
