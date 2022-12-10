
def checkout(days: int) -> int:
    week = int(days / 7);
    dayRemain = int(days % 7);
    print("Khách ở {} ngày = {} tuần và {} ngày".format(days, week, dayRemain));
    print("Vậy tiền phòng của khách = {} * 1.000.000 + {} * 200.000 = {} VNĐ".format(week, dayRemain, week * 1000000 + dayRemain * 200000));

day = int(input("Nhập vào số ngày ở: "));
checkout(day);