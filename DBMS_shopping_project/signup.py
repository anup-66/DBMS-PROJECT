import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin@1",
    database="shopping"
)


class Signup:
    def signup(self, username: str, password: str, name: str, mobile: int):
        crsr = mydb.cursor()
        crsr.execute('select username from customer;')
        res = crsr.fetchall()
        print(res)
        if res and username in [user[0] for user in res]:
            return 1
        else:
            create_client =f"create user '{username}'@'localhost' identified by '{password}';"
            crsr.execute(create_client)
            print(create_client)
            print(password,type(password))
            grant_user = f"grant select on shopping.* To '{username}'@'localhost';"
            crsr.execute(grant_user)
            crsr.execute("flush privileges;")
            mydb.commit()
            string = f"Insert into customer values('{username}','{password}','{name}',{mobile});"
            crsr.execute(string)
            mydb.commit()
            create_cart =f"create table cart_{username} ( id int auto_increment primary key ,productId int ,quantity int default 1 ,foreign key (productId) references products(productId))auto_increment=1001;"
            crsr.execute(create_cart)
            mydb.commit()
            create_wishlist = f"create table wishlist_{username} ( Wid int  auto_increment primary key,productId int,foreign key (productId) references products(productId))auto_increment=10001;"
            crsr.execute(create_wishlist)
            mydb.commit()
            crsr.close()
            return 0
