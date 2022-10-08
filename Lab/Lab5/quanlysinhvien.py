from colorama import Cursor
import pyodbc

connectionString = ''' DRIVER={SQL Server};
SERVER=DESKTOP-DIIHU0F;DATABASE=QLSinhVien;Trusted_Connection=yes;'''


def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn


def close_connection(conn):
    if conn:
        conn.close()


def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM Lop"
        cursor.execute(select_query)
        records = cursor.fetchall()
        print(f"Danh sách lớp là: ")
        for row in records:
            print("*"*50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã xảy ra lỗi! Lỗi >> ", error)


def get_all_sinh_vien():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM SinhVien")
        records = cursor.fetchall()
        print("Danh sách tất cả sinh viên là: ")
        print(f"Mã số\t\tHọ tên\t\t\t\t\tMã lớp")
        for row in records:
            print(f"{row[0]}\t\t{row[1]}\t\t\t\t\t {row[2]}")
    except (Exception, pyodbc.Error) as error:
        print("Đã xảy ra lỗi! Lỗi >> ", error)


# get_all_class()
get_all_sinh_vien()
