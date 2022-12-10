from datetime import datetime

year = int(input("Nhập vào năm sinh của bạn: "));
print("Nếu bạn sinh năm {} thì năm nay bạn {} tuổi".format(year, int(datetime.today().year) - year));