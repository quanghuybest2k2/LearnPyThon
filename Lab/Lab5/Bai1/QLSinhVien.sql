create DATABASE QLSinhVien
go
use QLSinhVien
go
CREATE TABLE Lop(
	ID int NOT NULL PRIMARY KEY,
	TenLop nvarchar(20) NOT NULL)
go
CREATE TABLE SinhVien(
	ID int NOT NULL PRIMARY KEY,
	HoTen nvarchar(100) NOT NULL,
	MaLop int REFERENCES Lop(ID)
)
go
INSERT Lop (ID, TenLop) VALUES (1, N'CTK43')
INSERT Lop (ID, TenLop) VALUES (2, N'CTK44A')
INSERT Lop (ID, TenLop) VALUES (3, N'CTK44B')
INSERT Lop (ID, TenLop) VALUES (4, N'CTK45A')
go
INSERT SinhVien (ID, HoTen, MaLop) VALUES (1, N'Trần Văn Thái wewr', 1)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (2, N'Mai Thành Thân', 2)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (3, N'Phạm Thanh Thảo', 2)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (4, N'Trần Quốc Bảo Trung', 3)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (5, N'Thái Thành Lam', 3)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (6, N'Trần Văn Tám', 3)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (7, N'Nguyễn Công Thành', 4)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (8, N'Nguyễn Thị Lụa', 1)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (9, N'Phan Thanh Nga', 1)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (10, N'Trương Công Quyền', 4)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (11, N'Võ Thị Sáu', 1)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (12, N'Võ Tòng', 2)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (13, N'Đinh Thành Trung', 2)
INSERT SinhVien (ID, HoTen, MaLop) VALUES (14, N'Nguyễn Bảo Trung', 3)
go
CREATE PROC InsertStudent
	@Id int,
	@HoTen nvarchar(100),
	@MaLop int
AS
BEGIN
	INSERT INTO SinhVien
	VALUES (@Id, @HoTen, @MaLop)
END
go
SELECT * FROM Lop
SELECT * FROM Lop WHERE ID = 1
SELECT * FROM SinhVien
SELECT sv.ID, sv.HoTen, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop
SELECT sv.ID, sv.HoTen, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop AND l.ID = 3
SELECT sv.ID, sv.HoTen, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop AND l.ID = 3 AND sv.HoTen LIKE '%Trung'
go