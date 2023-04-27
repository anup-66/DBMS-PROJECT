import mysql.connector


class Add:

    def add_wishlist(self, username: str, password: str, id: int):
        mydb = mysql.connector.connect(
            host="localhost",
            user='admin',
            password="admin@1",
            database='shopping'
        )
        try:
            crsr = mydb.cursor()
            print(id)
            # crsr.execute(f"select productid from wishlist_{username};")
            # res = crsr.fetchall()
            # print(res)
        # if  id in [a[0] for a in res]:
            crsr.execute(f"insert into wishlist_{username} (productId) values({id});")
            result = crsr.fetchall()
            mydb.commit()
            print(result)
            return True
        except mysql.connector.Error as e:
            print(e)
            return False

    def add_cart(self, username: str, password: str, id: int):
        mydb = mysql.connector.connect(
            host="localhost",
            user='admin',
            password="admin@1",
            database='shopping'
        )
        try:
            crsr = mydb.cursor()
            crsr.execute(f"select productid from cart_{username};")
            res = crsr.fetchall()
            print(id)
            # if id not in [a[0] for a in res]:
            crsr.execute(f"insert into cart_{username} (productId,quantity) values({id},{1});")
            result = crsr.fetchall()
            mydb.commit()
            print(result)
            return True
        except mysql.connector.Error as e:
            print(e)
            return False
    def buy_now(self, username: str, password: str, id: int):
        mydb = mysql.connector.connect(
            host="localhost",
            user='admin',
            password="admin@1",
            database='shopping'
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