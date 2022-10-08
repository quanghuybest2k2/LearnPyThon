import sqlite3
import pyodbc

connectionString = ''' DRIVER={SQL Server};
SERVER=DESKTOP-DIIHU0F;DATABASE=QLSinhVien;Trusted_Connection=yes;'''


def get_connection():
    connection = sqlite3().connect('QLSinhVien.db')
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select sqlite3_version();")
        db_version = cursor.fetchone()
        print("Bạn đang sử dụng sqlite3 phiên bản: ", db_version)
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Đã xảy ra lỗi!", error)


read_database_version()
