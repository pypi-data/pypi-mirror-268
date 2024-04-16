import pymysql


class DB:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.connect()

    def connect(self):
        self.connection = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="main", charset="utf8")
        self.cursor = self.connection.cursor()

    def get(self, name, table):
        self.cursor.execute(f"SELECT * FROM `{table}` WHERE `name` = '{name}';")
        return self.cursor.fetchone()

    def insert(self, table, into, values):
        self.cursor.execute(f"INSERT INTO `{table}`({','.join(into)}) VALUES ({','.join(values)})")
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
