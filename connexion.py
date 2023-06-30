import pymysql

class Database:
    def __init__(self, host, port, user, password, database):
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.connection.cursor()

# Créez une instance de la classe Database avec vos paramètres de connexion


db = Database("localhost", 3306, "root", "sandradeb", "CLIENT")