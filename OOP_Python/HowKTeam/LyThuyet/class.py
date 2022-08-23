# Bài 1
class SieuNhan:  # class SieuNhan đang chạy ở hàm __main__
    # khởi tạo constructor
    def __init__(self, ten: str, vuKhi: str, mauSac: str):
        self.ten = ten
        self.vukhi = vuKhi
        self.mauSac = mauSac

    def xinChao(self):
        return "Xin chào ta là: " + self.ten


SieuNhanDo = SieuNhan("Siêu nhân đỏ", "Kiếm", "Đỏ")
SieuNhanVang = SieuNhan("Siêu nhân vàng", "Dao", "Vàng")
# khỏi tạo thuộc tính (python vẫn hiểu mặc dù không có trong class SieuNhan)
# SieuNhanDo.ten = "Siêu nhân đỏ"
print(SieuNhanDo.xinChao())
print(SieuNhanDo.ten)
print(SieuNhanDo.vukhi)
print(SieuNhanDo.mauSac)

# bôi dòng: dữ shift-> di chuyển mũi tên
# không định nghĩa hàm (rỗng): từ khóa pass
