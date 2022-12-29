from datetime import datetime


class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime):
        self.__maSo = maSo  # private
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso

    @property
    def hoTen(self):
        return self.__hoTen

    @hoTen.setter
    def hoTen(self, hoten):
        self.__hoTen = hoten

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @ngaySinh.setter
    def ngaySinh(self, ngaySinh):
        self.__ngaySinh = ngaySinh

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
     # tuong tu phuong thuc ghi de toString()

    def __str__(self):
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    # hanh vi doi tuong sinh vien

    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")


class DanhSachSV:
    def __init__(self):
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    # tim sinh vien theo mssv, neu co tra ve sinh vien
    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]
    # tim sinh vien theo mssv, neu co tra ve vi tri sv trong ds

    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1

    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    # tim sinh vien ten "Nam"

    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.rsplit(' ', 1)[-1] == ten]
    # tim nhung sinh vien sinh truoc 15/06/2000

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]


sv1 = SinhVien(2015597, "Đoàn Quang Huy",
               datetime.strptime("13/02/2002", "%d/%m/%Y"))
sv2 = SinhVien(7125215, "Nguyễn Thúc Thùy Tiên",
               datetime.strptime("13/02/2002", "%d/%m/%Y"))
sv3 = SinhVien(2161161, "Nguyễn Thanh Tùng",
               datetime.strptime("13/02/1994", "%d/%m/%Y"))
sv4 = SinhVien(2622772, "Lê Đại Hải Nam",
               datetime.strptime("13/02/2002", "%d/%m/%Y"))
sv5 = SinhVien(2272377, "Nam Nguyễn Gì Đó",
               datetime.strptime("13/02/2002", "%d/%m/%Y"))
sv6 = SinhVien(2252525, "Huy Là Tao",
               datetime.strptime("13/02/2002", "%d/%m/%Y"))
# sv.xuat()
ds = DanhSachSV()
ds.themSinhVien(sv1)
ds.themSinhVien(sv2)
ds.themSinhVien(sv3)
ds.themSinhVien(sv4)
ds.themSinhVien(sv5)
ds.themSinhVien(sv6)
ds.xuat()

msTim = int(input("Nhập vào mã số muốn tìm: "))
kq = ds.timSvTheoMssv(msTim)
print("Đã tìm thấy sinh viên có mã số: ", msTim)
for sv in kq:
    sv.xuat()
print(ds.timVTSvTheoMssv(msTim))  # vị trí của sinh viên, bắt đầu từ 0
# xoa sinh vien
msXoa = int(input("Nhập vào mã số muốn xóa: "))
ds.xoaSvTheoMssv(msXoa)
ds.xuat()
# tim ten Nam
ten = input("Nhập tên muốn tìm: ")
kq = ds.timSvTheoTen(ten)
print("Đã tìm thấy sinh viên có tên: ", ten)
for sv in kq:
    sv.xuat()
# tim truoc ngay sinh truoc 15/06/2000
ngay = datetime.strptime("15/06/2000", "%d/%m/%Y")
kqNgay = ds.timSvSinhTruocNgay(ngay)
print("Đã tìm thấy ngày sinh trước 15/06/2000: ")
for sv in kqNgay:
    sv.xuat()
