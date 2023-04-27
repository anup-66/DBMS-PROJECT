import mysql.connector


class Delete:

    def wishlistdelete(self, username: str, id: int) -> bool:
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin@1",
            database="shopping"
        )
        try:
            crsr = mydb.cursor()
            crsr.execute(f"select wid from wishlist_{username};")
            res = crsr.fetchall()
            print(id)
            if id in [a[0] for a in res]:
                crsr.execute(f"delete from wishlist_{username} where wid={id};")
                result = crsr.fetchall()
                mydb.commit()
                # print(result)
                return True
        except mysql.connector.Error as e:
            print(e)
            return False

    def cartdelete(self, username: str, id: int) -> bool:
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin@1",
            database="shopping"
        )
        try:
            crsr = mydb.cursor()
            crsr.execute(f"select id from cart_{username};")
            res = crsr.fetchall()
            print(id)
            if id in [a[0] for a in res]:
                crsr.execute(f"delete from cart_{username} where id={id};")
                result = crsr.fetchall()
                mydb.commit()
                # print(result)
                return True
        except mysql.connector.Error as e:
            print(e)
            return False
