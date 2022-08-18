# mảng ngẫu nhiên
arr = [4, 2, 5, 15, 20, 55, 100, 45, 9, 3, 2, 63]
# cau a: Xuât tất cả các số lẻ không chia hết cho 5
for i in arr:
    if i % 2 != 0:
        if i % 5 != 0:
            print(i)
# cau b: Xuất tất cả các số Fibonacci
