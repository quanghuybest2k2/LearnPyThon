from Cau5 import Animal, Dog, Cat, Animals
from tkinter import *

root = Tk()
root.title("Quản lý loài vật")

animals = Animals([])
gender = StringVar(None)


def addAnimal():
    if etName.get() == '' or etAge.get() == '':
        print("Vui lòng nhập đầy đủ thông tin")
        return
    else:
        animal = Animal(etName.get(), etAge.get(), gender.get())
        animals.add(animal)
        print("Thêm thành công!")
        printAnimals()


def printAnimals():
    print("Danh sách hiện tại:")
    for animal in animals.list:
        print("-----------")
        print(animal)


lblTitle = Label(root, text="THÔNG TIN LOÀI VẬT", fg="red")
lblName = Label(root, text="Tên con vật")
lblAge = Label(root, text="Tuổi")
etName = Entry(root)
etAge = Entry(root)
lblGender = Label(root, text="Giống")
rdMale = Radiobutton(root, text="Giống đực",
                     variable=gender, value="Giống đực")
rdFemale = Radiobutton(root, text="Giống cái",
                       variable=gender, value="Giống cái")
btnAdd = Button(root, text="Thêm", command=addAnimal)


lblTitle.grid(row=0, column=1, columnspan=2)
lblName.grid(row=1, column=0)
etName.grid(row=1, column=1, columnspan=2, sticky="W", padx=64)
lblAge.grid(row=2, column=0, sticky="W")
etAge.grid(row=2, column=1, columnspan=2, sticky="W", padx=64)
lblGender.grid(row=3, column=0, sticky="W")
rdMale.grid(row=3, column=1)
rdFemale.grid(row=3, column=2)
btnAdd.grid(row=4, column=2, columnspan=2, sticky="N")

root.mainloop()
