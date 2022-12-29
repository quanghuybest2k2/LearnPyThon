# cau 1: Đọc danh sách sinh viên từ tập tin (txt/csv)
file = open("OOP/Bai2/data.txt", "r", encoding="utf8")
read = file.readlines()
listSv = []
sv = []
for i in read:
    if i not in listSv:
        listSv.append(i.strip())
# print(listSv[0])
# for i in listSv:
#     # print(i.split(","))
#     sv.sort()
#     sv += i.split(",")
# print(sv)
listSv.sort()
print(listSv)

# cau 2: Sắp xếp danh sách sinh viên tăng/giảm theo họ tên
