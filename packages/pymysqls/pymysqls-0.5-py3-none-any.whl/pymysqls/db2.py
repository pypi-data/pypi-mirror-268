import pymysql


class DB:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.connect()

    def connect(self):
        """
        Подключиться к базе данных
        :return:
        """
        self.connection = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="calculatio", charset="utf8")
        self.cursor = self.connection.cursor()

    def get_id_by_name(self, name, table):
        """
        Получить id по имени из таблицы
        :param name: Значение name
        :param table: Имя таблиыч в базе данных
        :return: Результат поиска
        """
        self.cursor.execute(f"SELECT * FROM `{table}` WHERE `name` = '{name}';")
        return self.cursor.fetchone()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
