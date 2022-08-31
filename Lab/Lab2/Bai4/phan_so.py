class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau

    def __str__(self) -> str:
        return "{}/{}".format(self.tu, self.mau)

    @staticmethod
    # Dùng @staticmethod để self không được truyền mặc định vào tham số của hàm
    def __TimUCLN(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def RutGon(self):
        ucln = self.__TimUCLN(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def __add__(self, other):
        '''Cộng 2 phân số ps1 + ps2'''
        kq = PhanSo()
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __sub__(self, other):
        '''Trừ 2 phân số ps1 - ps2'''
        kq = PhanSo()
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __mul__(self, other):
        '''Nhân 2 phân số ps1 * ps2'''
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __truediv__(self, other):
        '''Chia 2 phân số ps1 / ps2'''
        kq = PhanSo()
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.RutGon()
        return kq


# x = PhanSo(4, 6)
# y = PhanSo(2, 3)
# z = x+y
# print(x+y)
# print(z)
ps1 = PhanSo(5, 7)
ps2 = PhanSo(4, 6)
ps3 = PhanSo(-2, 3)
ps4 = PhanSo(-5, 8)
ps5 = PhanSo(5, 8)


class DanhSachPhanSo():
    def __init__(self):
        self.dsps = []

    def ThemPhanSo(self, ps: PhanSo):
        self.dsps.append(ps)

    def xuat(self):
        for ps in self.dsps:
            print(ps)

    def DemPhanSo(self):
        listPS = [ps for ps in self.dsps if ps < 0]
        # for ps in self.dsps:
        #     if ps < 0:
        #         print(ps)
        print(listPS)


dsps = DanhSachPhanSo()
dsps.ThemPhanSo(ps1)
dsps.ThemPhanSo(ps2)
dsps.ThemPhanSo(ps3)
dsps.ThemPhanSo(ps4)
dsps.ThemPhanSo(ps5)
dsps.xuat()
dsps.DemPhanSo()
# for ps in kq:
#     ps.xuat()

# cau 1: Đếm số phân số âm trong mảng
