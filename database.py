import sqlite3
class Database:
    def query(self,query):
        self.sqlite_connection = sqlite3.connect("database/urls.db")
        self.cursor = self.sqlite_connection.cursor()
        try:
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            self.sqlite_connection.commit()
            self.cursor.close()
            return record
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (self.sqlite_connection):
                self.sqlite_connection.close()
                print("Соединение с SQLite закрыто")

database = Database()

class WorkDatabase:
    @staticmethod
    def createSrcInDatabase(hex,url,views=0):
        database.query("INSERT INTO url ('hex','url','views') VALUES ('{}','{}','{}');".format(hex,url,views))

    @staticmethod
    def checkSrcInDatabase(hex):
        hex = database.query("SELECT id FROM url WHERE hex='{}';".format(hex))
        if hex == []:
            return True
        return False

    @staticmethod
    def getHexAndSrc(hex):
        hex,src = database.query("SELECT hex,url FROM url WHERE hex='{}';".format(hex))[0]
        return (hex,src)

    @staticmethod
    def getViews(hex):
        views = database.query("SELECT views FROM url WHERE hex='{}';".format(hex))[0]
        return views[0]

    @staticmethod
    def AddView(hex):
        views = database.query("UPDATE url SET views = views + 1 WHERE hex='{}';".format(hex))
