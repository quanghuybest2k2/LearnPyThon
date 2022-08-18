# không đệ quy

def fibonacci(n):
    f0 = 0
    f1 = 1
    fn = 1

    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn


input = int(input("Nhập vào n: "))
sb = ""
for i in range(0, input):
    sb = sb + str(fibonacci(i)) + ", "
print(sb)

# đệ quy


def fibonacci(n):
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


input = int(input("Nhập vào n: "))
sb = ""
for i in range(0, input):
    sb = sb + str(fibonacci(i)) + ", "
print(sb)
