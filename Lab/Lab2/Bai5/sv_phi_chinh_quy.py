from sinh_vien import SinhVien
from datetime import datetime

class SinhVienPhiCQ(SinhVien):
    def __init__(self, maSo:int, hoTen:str, ngaySinh:datetime, trinhdo:str, tgdt:int):
        super().__init__(maSo, hoTen, ngaySinh)
        self.thoiGianDaoTao = tgdt
        self.trinhdo = trinhdo

    def __str__(self)->str:
        return super().__str__()+f"{self.trinhdo}\t{self.thoiGianDaoTao}"
    