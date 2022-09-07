from tkinter import Button, Tk, Frame, BOTH
from tkinter.ttk import Style


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        self.parent = parent  # thuộc tính parent để lưu đối tượng root
        self.initUI()  # tao các widget trên cửa sổ

    def initUI(self):
        self.parent.title("Chương trình đầu tiên")
        self.pack(fill=BOTH, expand=1)
        self.style = Style()
        # ('clam', 'alt', 'default', 'classic')
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Thoát", command=self.quit)
        quitButton.place(x=50, y=50)


root = Tk()  # tao cua so
root.geometry("650x350+100+100")  # size(width x height + x + y)
app = Example(root)
root.mainloop()
