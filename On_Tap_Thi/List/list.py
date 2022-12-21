# Theo cá nhân tao thì list là mảng, mục đích là lưu trữ nhiều value trong một biến
# tạo list
name = ["Huy", "Hoa", "Lan", "Vân"]  # [0, 1, 2, 3]
# python cho phép trùng lặp value (ngươc với set)
name_trung = ["Huy", "Hoa", "Huy", "Vân"]  # [0, 1, 2, 3]
print(name_trung)
print(f"Độ dài của list: {len(name)}")
# có thể khác kiểu dữ liệu trong một list
list_world = ["Người yêu cũ", 2, ["Con người", "Động vật", "Thực vật"], True]
print(list_world)
# list() constructor
list_constructor = list((1, 2, 3, 5))
print(list_constructor)
# lấy item list[index]
print(list_world[0])  # Người yêu cũ
# lấy ngược item list[-index]
print(list_world[-1])  # -1 là phần tử cuối cùng vì méo có -0, kq = True
# lấy item trong khoảng list
print(list_world[1:3])  # lấy vị trí thứ 1 đến 3 (không tính vị trí số 3)
# lấy từ đầu đến 2 (không tính vt 2)
print(list_world[:2])  # ['Người yêu cũ', 2]
# lấy từ vt 2 đến cuối
print(list_world[2:])  # [['Con người', 'Động vật', 'Thực vật'], True]
# lấy ngược cũng tương tự
print(list_world[-3:-1])  # [2, ['Con người', 'Động vật', 'Thực vật']]
# thay đổi giá trị thứ 0
list_world[0] = "Ai cũng được"
print(list_world)
# sua vi tri trong khoang
list_world[0:2] = ["Huy", 3]
print(list_world)
# chèn item (vt, value)
list_world.insert(0, "Hi hi")
print(list_world)
# them(noi) item
list_world.append("Them Item")
print(list_world)
# noi list
name.extend(list_world)
print(name)
# xoa item trong list
list_world.remove("Huy")
print(list_world)
# xoa theo vi tri index, neu không truyền vị trí list_world.pop() sẽ xóa phần tử cuối
list_world.pop(3)
print(list_world)
# loop list
# for i in list_world:
#     print(i)
for i in range(len(list_world)):
    print(list_world[i])
