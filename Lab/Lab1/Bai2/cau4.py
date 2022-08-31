# # in ra dãy số từ input, vd 4 => 0 1 1 2 3

# N = int(input("Enter the number of terms : "))

# # first two terms are f1, f2 equal to 0 and 1 respectively
# f1, f2 = 0, 1
# count = 0

# # checking for invalid inputs
# if(N <= 0):
#     print("Invalid Input, Kindly enter number greater than 0")

# # if only one number in the sequence
# elif(N == 1):
#     print("Generating Fibonacci Sequence upto ", N, ": ")
#     print(f1)

# # for all the other cases, i.e. when N > 1
# else:
#     print("Generating Fibonacci sequence upto ", N, ": ")
#     while count < N:
#         print(f1)
#         fth = f1 + f2
# # swapping the values for f1 and f2
#         f1 = f2
#         f2 = fth
#         count += 1

# Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không

N = int(input("Nhập vào số bạn muốn kiểm tra: "))

# variables for generating fibonacci sequence
f3 = 0
f1 = 1
f2 = 1
# 0 and 1 both are fibonacci numbers
if (N == 0 or N == 1):
    print("Đây là số trong dãy fibonacci")

else:
    # generating the fibonacci numbers until the generated number is less than  N
    while f3 < N:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
    if f3 == N:
        print("Đây là số trong dãy fibonacci")
    else:
        print("Không phải số trong dãy fibonacci")
