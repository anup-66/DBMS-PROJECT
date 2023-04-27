import mysql.connector
class Cart:
    def cart(self,username:str,password:str):
        mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database='shopping'
        )
        crsr = mydb.cursor()
        execute = f"select cart_{username}.id, products.productid ,  " \
                  f" products.productname, products.productprice, sellerinfo.sellername from products , cart_{username}, sellerinfo where products.productID=cart_{username}.productId and sellerinfo.sellerId=products.sellerid;"
        crsr.execute(execute)
        res = crsr.fetchall()
        # print("sssssssssssssssssssssssssssssssss")
        print(res)
        crsr.close()
        return res
# mm = wishlist()
# val = mm.wishlist('aditi11','aditi@11')
# print(val)