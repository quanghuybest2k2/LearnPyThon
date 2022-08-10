# variable
import datetime
#ten = "Đoàn Quang Huy"
#tuoi = 19
#print(ten, tuoi)

# calculator your age
name = input("what is your name?\n")
#getCurrentDay = currentDay.strftime("%d/%m/%Y")
currentDay = datetime.datetime.now()
YearofBirth = input("What year were born?\n")
age = currentDay.year - int(YearofBirth)
# f trước chuỗi để truyền biến hoặc dùng format()
print(f"Your name: {name}, Your age: {age}")
print("Hi {}, you are {}".format(name, age))
print("Hi {name}, you are {age}".format(name=name, age=age))
