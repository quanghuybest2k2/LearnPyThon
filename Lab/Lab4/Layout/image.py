from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Hinh anh")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", bg="#333")

        bard = Image.open("Layout/img/Huy.jpg")
        bard = bard.resize((100, 100), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard)
        lable1 = Label(self, image=bardejov)
        lable1.image = bardejov
        lable1.place(x=20, y=20)


root = Tk()
root.geometry("300x280+300+300")
app = Example(root)
root.mainloop()
