# mảng ngẫu nhiên
from cmath import sqrt
import math
import sys
from operator import truediv
arr = [4, 2, 5, 15, 20, 55, 45, 7, 9, 3, 2, 63]
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
