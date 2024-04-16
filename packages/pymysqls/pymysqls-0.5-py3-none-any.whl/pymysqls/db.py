import mysql.connector

host = '46.188.59.18'
user = 'service_yvu'
password = 'd1Ha6rmu5Q/eDOwZ'
database = 'service_yvu'


class DB:
    def __init__(self):
        self.con = self.connect_to_mysql()

    def __del__(self):
        if self.con is not None:
            print("Отключение от БД...")
            self.con.close()

    def connect_to_mysql(self):
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            print("Подключение к БД...")
            return connection
        except Exception as e:
            print("Ошибка при подключении.", e)
            return None
