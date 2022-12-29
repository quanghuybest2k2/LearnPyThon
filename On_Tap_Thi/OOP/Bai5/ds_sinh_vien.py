from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien
from datetime import datetime


class DanhSachSv:
    def __init__(self):
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def ReadFile(self, path: str) -> None:
        line = ""
        with open(path, "r", encoding="utf8") as fileReader:
            while (line := fileReader.readline()) != "":
                sv = ""
                s = line.split("*")
                if s[0] == "CQ":
                    sv = SinhVienChinhQuy(int(s[1]), s[2], datetime.strptime(
                        s[3], "%d/%m/%Y"), int(s[4]))
                else:
                    sv = SinhVienPhiCQ(int(s[1]), s[2], datetime.strptime(
                        s[3], "%d/%m/%Y"), s[4], float(s[5]))
                self.themSV(sv)
        fileReader.close()

    def __str__(self):
        s = f"{'MSSV':<16}{'HỌ VÀ TÊN':<24}{'NGÀY SINH':<20}{'TRÌNH ĐỘ (PCQ)':<20}{'RL (CQ)'}{'TGĐT (PCQ)':>15}\n"
        "========================================================================================================\n"
        for sv in self.dssv:
            s += "{}\n".format(sv)
        return s

    def timSVTheoMs(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ms:
                return i
        else:
            return -1

    def timSvTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]

    @staticmethod
    def KiemTraSVCoDRL80(sv: SinhVien):
        if not isinstance(sv, SinhVienChinhQuy):
            return False
        if sv.DiemRL >= 80:
            return True
        return False

    def TimSVCoDiemRenLuyen80(self):
        return [sv for sv in self.dssv if self.KiemTraSVCoDRL80(sv)]

    @staticmethod
    def KiemTraSVCongaysinhtrc(sv: SinhVien):
        if not isinstance(sv, SinhVienPhiCQ):
            return False
        if sv.TrinhDo.lower() == "Cao đẳng".lower() and sv.ngaySinh < datetime.strptime("15/8/1999", "%d/%m/%Y"):
            return True
        return False

    def TimSVsinhtrcngay(self):
        return [sv for sv in self.dssv if self.KiemTraSVCongaysinhtrc(sv)]
