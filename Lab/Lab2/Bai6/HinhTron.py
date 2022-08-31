import math
from posixpath import basename
from HinhHoc import HinhHoc


class HinhTron(HinhHoc):

    def __init__(self, bankinh: float) -> None:
        super().__init__(bankinh)

    def TinhDienTich(self) -> float:
        return pow(self.banKinh) * math.pi

    def xuat(self):
        print(self.banKinh, self.tinhDienTich())

    @property
    def banKinh(self):
        return self._canh


ht = HinhTron(5)
ht.tinhDienTich(7)
# ht.xuat()
