a = int(input("Nhập vào số thứ nhất: "));
b = int(input("Nhập vào số thứ hai: "));
while(True):
    if (b < a):
        (a, b) = (b, a);
    num = int(input("Nhập vào một số trong đoạn [{}, {}]: ".format(a, b)));
    if num >= a and num <= b:
        break;
print("Kết quả của số {} chia cho 3 là {}".format(num, round((num / 3), 2)));