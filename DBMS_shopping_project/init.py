from flask import Flask, session, url_for
import mysql.connector
from flask import render_template, request, redirect
from signup import Signup
from wishlist import Wishlist
from cart import Cart
from search import Search
from add import Add
from delete import Delete
app = Flask(__name__)
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="admin",
#     password="admin@1",
#     database="shopping"
# )
#
# # create a cursor object
# mycursor = mydb.cursor()

# User = ""
# Pass = ""
app.secret_key = 'Anup'


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if not request.method=='GET':
        global User
        global Pass
        # return render_template("client.html")
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin@1",
            database="shopping"
        )
        mycursor = mydb.cursor()
        username = request.form['username']
        password = request.form['password']
        session['User'] = username
        session['Pass'] = password
        mycursor.execute('select username,password from customer;')
        result = mycursor.fetchall()
        # print(User,Pass)
        print(result)
        if username == 'admin' and password == 'admin@1':
            print("thgythgythgythgythgythgythgy")
            # return redirect(url_for('Admin'))
            # return "admin"
            return render_template("admin.html")
        elif username in [user[0] for user in result]:
            Str = "select password from customer where username = %s;"
            mycursor.execute(Str, (username,))
            passResult = mycursor.fetchall()
            print(passResult)
            if passResult and password == str(passResult[0][0]):
                return render_template("client.html",msg="")
                # return "client1"
            else:
                return render_template('login.html', msg="Please enter correct password")
        else:
            return render_template('login.html', msg='you are not registered please signup first')
    else:
        redirect(url_for('login'))
    return render_template('login.html',msg='')

@app.route('/admin')
def Admin():
    print("here it is")
    return render_template('admin.html')

@app.route('/signup', methods=['POST'])
def signup():
    return render_template("signup.html")

@app.route('/admin',methods = ['GET','POST'])
def admin():
    print("no it his here")
    query = request.form['text']
    src = Search()
    result,columns = src.query(query)
    return render_template('admin.html',msg=result,List=columns)

@app.route('/detail', methods=['GET', 'POST'])
def signup_detail():
    username = request.form['username']
    password = request.form['password']

    name = request.form['name']
    mobile = int(request.form['mobile'])
    print(username, password, name, mobile)
    Sign = Signup()
    result = Sign.signup(username, password, name, mobile)
    if not result:
        return render_template('login.html', msg="singed up successfully.")
    else:
        return render_template('login.html', msg="You already have a account.")


@app.route('/client', methods=['GET', 'POST'])
def client():
    return render_template("client.html", msg="")


@app.route('/wishlist', methods=['GET', 'POST'])
def wishlist():
    wish = Wishlist()
    items = wish.wishlist(session['User'], session['Pass'])
    # print(session['User'],session['Pass'])
    print(items)
    # items = [("mobile", 23, "sss"), ("tv", 43, "aaa")]
    return render_template('wishlist.html', items=items)


@app.route('/wishlist/add/<item>', methods=['GET','POST'])
def add_to_wishlist(item):
    print(item)
    toAdd = Add()
    value = toAdd.add_wishlist(session['User'], session['Pass'],int(item))
    wish = Wishlist()
    items = wish.wishlist(session['User'], session['Pass'])

    if value:
        return render_template("wishlist.html", items = items)
    else:
        return redirect(url_for('search'))


@app.route('/cart', methods=['POST'])
def cart():
    # items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']  # Replace this with your actual list of items
    cart = Cart()
    items = cart.cart(session['User'], session['Pass'])
    # print("item ; " , items)
    return render_template('cart.html', items=items)



@app.route('/cart/buy/<item>', methods=['POST'])
def to_buy_now(item):
    print(item)
    tobuy = Add()
    value = tobuy.buy_now(session['User'], session['Pass'], int(item))
    cart = Cart()
    items = cart.cart(session['User'], session['Pass'])

    # if value:
        # return render_template("cart.html", items=items)
    return render_template("cart.html",items = items)
    # else:
    #     return redirect(url_for(f'/cart/buy/{item}'))


@app.route('/cart/add/<item>', methods=['GET','POST'])
def add_to_cart(item):
    print(item,"jiijjiji")
    toAdd = Add()
    value = toAdd.add_cart(session['User'], session['Pass'],int(item))
    cart = Cart()
    items = cart.cart(session['User'], session['Pass'])

    if value:
        return render_template("cart.html", items = items)
    else:
        return redirect(url_for('search'))


@app.route('/wishlist/delete/<item>', methods=['GET','POST'])
def delete_from_wishlist(item):
    print(item,"jiijjiji")
    todelete = Delete()
    value = todelete.wishlistdelete(session['User'],int(item))
    wish = Wishlist()
    items = wish.wishlist(session['User'], session['Pass'])

    if value:
        return render_template("wishlist.html", items = items)
    else:
        return redirect(url_for('search'))



@app.route('/cart/delete/<item>', methods=['GET','POST'])
def delete_from_cart(item):
    print(item,"jiijjiji")
    todelete = Delete()
    value = todelete.cartdelete(session['User'],int(item))
    cart = Cart()
    items = cart.cart(session['User'], session['Pass'])

    if value:
        return render_template("cart.html", items = items)
    else:
        return redirect(url_for('search'))

@app.route('/search', methods=['POST'])
def search():
    searchReasult = request.form['search']
    print(searchReasult)
    Search_item = Search()
    results = Search_item.searchitems(session['User'], session['Pass'], searchReasult)
    return render_template('client.html', msg=results)


@app.route('/allitem', methods=['GET','POST'])
def allitem():
    find = Search()
    findlist = find.searchAllItems(session['User'], session['Pass'])
    return render_template('client.html', msg=findlist)


@app.route('/myinfo',methods = ['GET','POST'])
def myinfo():
    myinfo = Search()
    result = myinfo.info(session['User'], session['Pass'])
    print(result[0][2])
    return render_template('myinfo.html',name=result[0][0],username=result[0][1],mobile=result[0][2])


if __name__ == '__main__':
    app.run(debug=True)
