from tkinter import *
from tkinter.ttk import *

root = Tk()

# mssv
lbl_mssv = Label(root, text="Mã số sinh viên:")
lbl_mssv.grid(row=0, column=0, sticky=W, pady=2)
entry_mssv = Entry(root)
entry_mssv.grid(row=0, column=1, pady=2)
# ho ten
lbl_HoTen = Label(root, text="Họ tên:")
lbl_HoTen.grid(row=1, column=0, sticky=W, pady=2)
entry_HoTen = Entry(root)
entry_HoTen.grid(row=1, column=1, pady=2)
# ngay sinh
lbl_NgaySinh = Label(root, text="Ngày sinh:")
lbl_NgaySinh.grid(row=2, column=0, sticky=W, pady=2)
entry_NgaySinh = Entry(root)
entry_NgaySinh.grid(row=2, column=1, pady=2)
# email
lbl_Email = Label(root, text="Email: ")
lbl_Email.grid(row=3, column=0, sticky=W, pady=2)
entry_Email = Entry(root)
entry_Email.grid(row=3, column=1, pady=2)
# So dien thoai
lbl_SDT = Label(root, text="Số điện thoại: ")
lbl_SDT.grid(row=4, column=0, sticky=W, pady=2)
entry_SDT = Entry(root)
entry_SDT.grid(row=4, column=1, pady=2)
# hoc ky
lbl_HocKy = Label(root, text="Học kỳ: ")
lbl_HocKy.grid(row=5, column=0, sticky=W, pady=2)
entry_HocKy = Entry(root)
entry_HocKy.grid(row=5, column=1, pady=2)
# nam hoc
lbl_NamHoc = Label(root, text="Năm học: ")
lbl_NamHoc.grid(row=6, column=0, sticky=W, pady=2)
cbb_NamHoc = Combobox(root)
cbb_NamHoc.grid(row=6, column=1, pady=2)
# chon mon hoc
# tao frame mới
lbl_ChonMonHoc = Label(root, text="Chọn môn học: ")
lbl_ChonMonHoc.grid(row=7, column=0, sticky=W, pady=1)
# lap tinh python
# chkPython = Checkbutton(root)
# chkPython.grid(row=7, column=1, pady=2)
# lbl_python = Label(root, text="Lập trình Python")
# lbl_python.grid(row=7, column=2, sticky=W, pady=2)

root.geometry("300x300+300+300")
root.mainloop()
