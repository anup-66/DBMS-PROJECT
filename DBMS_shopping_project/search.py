import MySQLdb
import mysql.connector


class Search:
    def searchitems(self, username: str, password: str, search: str) -> list:
        mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database='shopping'
        )
        crsr = mydb.cursor()
        crsr.execute(f"select * from products where productName LIKE '%{search}%';")
        result = crsr.fetchall()
        return result

    def searchAllItems(self, username: str, password: str) -> list:
        mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database='shopping'
        )
        crsr = mydb.cursor()
        crsr.execute(f"select * from products;")
        result = crsr.fetchall()
        return result

    def info(self, username: str, password: str):
        mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database='shopping'
        )
        crsr = mydb.cursor()
        try:
            crsr.execute(f"select customerName, username , customerMobile from customer where username='{username}';")
            result = crsr.fetchall()
            return result
        except mysql.connector.Error as error:
            return [f"MySQL Error: {format(error)}"]
        finally:
            crsr.close()
            crsr.close()
        # return result

    def query(self, query: str):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin@1",
            database="shopping"
        )
        crsr = mydb.cursor()
        try:
            crsr.execute(query)
            result = crsr.fetchall()
            columns = [i[0] for i in crsr.description]
            mydb.commit()
            if result:
                return result,columns
            else:
                return ["Your Query successfully executed.😊😊"]
        except mysql.connector.Error as error:
            return [f"MySQL Error: {format(error)}"]
        finally:
            crsr.close()

# mo = Search()
# res = mo.searchitems('aditi11','aditi@11','f')
# print(res)
