# mảng ngẫu nhiên
from cmath import sqrt
import math
import sys
from operator import truediv
arr = [4, 2, 5, 15, 20, 55, 45, 7, 3, 9, 3, 2, 63, 3, 3, 5]
# cau a: Xuât tất cả các số lẻ không chia hết cho 5
for i in arr:
    if i % 2 != 0:
        if i % 5 != 0:
            print(i)
# cau b: Xuất tất cả các số Fibonacci


def isPerfectSquare(num):

    n = int(math.sqrt(num))
    return (n * n == num)


def checkFib(array, n):

    count = 0
    for i in range(n):

        if (isPerfectSquare(5 * array[i] * array[i] + 4) or
                isPerfectSquare(5 * array[i] * array[i] - 4)):

            print(array[i], " ", end="")
            count = count + 1
    print()
    if (count == 0):
        print("None present")


n = len(arr)

checkFib(arr, n)

# cau c: Tìm số nguyên tố lớn nhất


def Prime(arr, n):
    max_val = max(arr)
    prime = [True for i in range(max_val + 1)]
    prime[0] = False
    prime[1] = False
    for p in range(2, math.ceil(math.sqrt(max_val))):
        if (prime[p] == True):
            for i in range(2 * p, max_val + 1, p):
                prime[i] = False
    # minimum = 10**9
    maximum = -10**9
    for i in range(n):
        if (prime[arr[i]] == True):
            # maximum = min(maximum, arr[i])
            maximum = max(maximum, arr[i])
    print("Maximum : ", maximum)


n = len(arr)

Prime(arr, n)

# cau d: Tìm số Fibonacci bé nhất


def createHash(hash, maxElement):
    prev = 0
    curr = 1
    hash.add(prev)
    hash.add(curr)
    while (curr <= maxElement):
        temp = curr + prev

        hash.add(temp)
        prev = curr
        curr = temp


def fibonacci(arr, n):
    max_val = max(arr)
    hash = set()
    createHash(hash, max_val)
    minimum = sys.maxsize
    maximum = -sys.maxsize-1
    for i in range(n):
        if (arr[i] in hash):
            minimum = min(minimum, arr[i])
            maximum = max(maximum, arr[i])
    print("Số fibonacci bé nhất là: ", minimum)
    n = len(arr)


fibonacci(arr, n)
# cau e:  Tính trung bình các số lẻ
count = 0
n = 0
for i in arr:
    if i % 2 != 0:
        count += i
        n += 1
tong = count / n
print("Trung bình cộng các số lẽ là: ", tong)

# cau f: Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng
prod = 1
for i in arr:
    if i % 3 != 0 and i % 2 != 0:
        print("ket qua", i)
        prod *= i
print("ket qua", prod)
# cau g: Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ


def swapList(sl, pos1, pos2):
    n = len(sl)
    temp = sl[pos1]
    sl[pos1] = sl[pos2]
    sl[pos2] = temp
    return sl


pos1 = int(input("Nhap vao vi tri dau tien: "))
pos2 = int(input("Nhap vao vi tri thu hai: "))

print(arr)
print("Sau khi hoan doi: ", swapList(arr, pos1-1, pos2-1))
# Cau h: Đảo ngược trật tự các phần tử của danh sách
reducer = len(arr)
Reversed_list = [arr[reducer] for reducer in range(reducer - 1, -1, -1)]
print("danh sach sau khi dao nguoc", Reversed_list)

# cau i: Xuất tất cả các số lớn thứ nhì của danh sách


def Find_max_second(a):
    max_1 = max(a[0], a[1])
    max_2 = min(a[0], a[1])

    for i in range(2, len(a)):
        if a[i] > max_1:
            max_2 = max_1
            max_1 = a[i]
        elif (a[i] > max_2) and (max_1 != a[i]):
            max_2 = a[i]

    return max_2


print("\nPhan tu lon thu hai trong danh sach tren la:", Find_max_second(arr))

# cau j: Tính tổng các chữ số của tất cả các số trong danh sách
sum = 0
for i in arr:
    sum += i
print("Tong tat ca cac so la: ", sum)

# cau k: Đếm số lần xuất hiện của một số trong danh sách
XuatHien = int(input("Nhap vao so muon tim: "))
print(f"So lan xuat hien cua {XuatHien} la: ", arr.count(XuatHien))

# cau l: Xuất các số xuất hiện n lần trong danh sách

SLXuatHien = int(input("Nhap vao so lan xuat hien: "))
list = []
for i in arr:
    if SLXuatHien == arr.count(i):
        print(SLXuatHien)

# cau m: Xuất các số xuất hiện nhiều lần nhất trong danh sách


def most_frequent(arr):
    counter = 0
    num = arr[0]

    for i in arr:
        curr_frequency = arr.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


print("Xuat hien nhieu nhat: ", most_frequent(arr))
