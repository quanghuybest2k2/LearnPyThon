
import time


x = "  hello"
y = x.strip()
print(y)
print(type(x))
age = 36
txt = "My name is Jonh, and I am {}"
print(txt.format(age))
print(bool("abc"))
print(10 == 9)
if 5 == 10 or 4 == 4:
    print("tests")
print(10//4)
sum = 0
for i in range(1, 10, 2):
    sum += i
print(sum)
x = 0
while x < 5:
    print(x)
    x += 1
sum2 = 0
for i in range(5):
    sum2 += i
print("tong: ", sum2)
fruits = ["apple", "banana", "cherry"]
# fruits[1] = "kiwi"
# fruits.insert(2, "lemon")
# fruits.append("lemon")
set = {"apple", "banana", "cherry"}
set.discard("banana")

print("ket qua list: ", fruits)
print("ket qua set: ", set)
print("Phan tu cuoi cung", fruits[-1])
xuat = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(xuat[2:5])
print(xuat[4:])
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.update({"color": "red"})
car["year"] = 2020
print(car)


list1 = [3, 4, 5, 20, 5, 25, 1, 3]
list1.pop(1)
print(list1)
time_sec = time.time()
print(time_sec)
print("Dalat university"[::-1])
print(0.1 + 0.2 == 0.3)
nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']
pos = nameList.index("Bob")
print(pos * 3)
D = dict()
for x in enumerate(range(2)):
    D[x[0]] = x[1]
    D[x[1]+7] = x[0]
print(D)


def my_function(* kids):
    print("The youngest child is " + kids[2])


d = ~~~~~~5
t = ~~~18
print(d)
print(t)
a = {i: i * i for i in range(6)}
print(a)  # {0:0, 1:1, 2:4, 3:9, 4:16, 5:25}
