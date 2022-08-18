# Tính tổng căn bậc 2 của n số nguyên đầu tiên
from cmath import sqrt

# Tính tổng căn bậc 2 của n số nguyên đầu tiên

sum = 0
n = int(input("Nhập vào n: "))
for i in range(0, n):
    sum += sqrt(i)
print(sum)
