# dictionary lưu trữ cặp key - value
idol = {"Name": "MTP", "Age": 27}  # các phần tử cách nhau bởi dấu phẩy
# độ dài của dic
print(len(idol))
print(idol["Name"])
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]  # list có thể lưu trữ trong Dic
}
x = thisdict.get("year")  # get a value
v = thisdict.values()  # get all value

y = thisdict.keys()  # get all keys
print(x)
print(v)
print(y)
