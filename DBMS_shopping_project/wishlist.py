import mysql.connector


class Wishlist:

    def wishlist(self, username: str, password: str):
        mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database='shopping'
        )
        crsr = mydb.cursor()
        execute = f"select products.productId, products.productName,products.productprice,sellerName ,wishlist_{username}.wid from products , " \
                  f"wishlist_{username}, sellerinfo where products.productID=wishlist_{username}.productId and " \
                  f"sellerinfo.sellerId=products.sellerid; "
        crsr.execute(execute)
        res = crsr.fetchall()
        # print(res)
        crsr.close()
        return res
# mm = wishlist()
# val = mm.wishlist('aditi11','aditi@11')
# print(val)
