import mysql.connector
from config import Config

class MySqlCoordinator:
    
    def __init__(self):
        self.mydb = mysql.connector.connect(**Config.SQL_CONFIG)
      
    def query_db(self, query):
        sql_cursor = self.mydb.cursor(dictionary=True)
        sql_cursor.execute(query)
        result = sql_cursor.fetchall()
        return result

    def query_db_one(self, query):
        sql_cursor = self.mydb.cursor(dictionary=True)
        sql_cursor.execute(query)
        result = sql_cursor.fetchone()
        return result 
    
    def write_db(self, query):
        sql_cursor = self.mydb.cursor(dictionary=True)
        result = sql_cursor.execute(query)
        self.mydb.commit()
        return result 
    