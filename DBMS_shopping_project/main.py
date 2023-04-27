import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin@1",
  database="shopping"
)
# crsr = mydb.cursor()
# crsr.execute("select * from customer;")
# # crsr.execute("delete from customer where username = 'Kiran_55';")
# result = crsr.fetchall()
# mydb.commit()
# print(result)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customer")

rows = mycursor.fetchall()
columns = [i[0] for i in mycursor.description]

print(columns)
for row in rows:
    print(row)