from flask import *
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=你的伺服器名稱;'
    'DATABASE=資料庫名稱;'
    'UID=帳號;PWD=密碼'
)

cursor = conn.cursor()

@app.route("/")
def first():        
    return render_template("first.html")

@app.route("/choice_identity",methods=['GET','POST'])
def choice_identity():
    if request.method == 'POST':
        button = request.form.get("choice")

        if button == "customer_entry":
            return render_template("customer_login.html")
        elif button == "store_entry":
            return render_template("store_login.html")
        
    return render_template("first.html")

@app.route("/login_customer",methods=['POST'])
def login_customer():    
    if request.method == 'POST':
        phone = request.form.get("phone")

        cursor.execute("SELECT phone FROM customer")
        rows = cursor.fetchall()

        for row in rows :
            if phone == row[0] :
                return render_template("customer_order.html")
            
    return render_template("customer_login.html")
    
@app.route("/login_store",methods=['GET','POST'])
def login_store():    
    if request.method == 'POST':
        store_id = request.form.get("store_id")

        cursor.execute("SELECT store_id FROM store")
        rows = cursor.fetchall()

        for row in rows :
            if store_id == row[0] :
                return render_template("order.html")
            
    return render_template("store_login.html")
    

@app.route("/product_name",methods=['POST'])
def product_name():    
    cursor.execute("SELECT product.name FROM product")
    rows = cursor.fetchall() 
    return render_template("order.html",items=rows)

@app.route("/customer_order",methods=['POST'])
def customer_order():    
    if request.method == 'POST':
        product_name = request.form.get("product_name")
        cursor.execute("SELECT photo FROM product WHERE name=?",(product_name,))
        rows = cursor.fetchall() 
        return render_template("order.html",items=rows)


    return render_template("order.html")

@app.route("/customer_order",methods=['POST'])
def login_store():    
    if request.method == 'POST':
        store_id = request.form.get("store_id")

        cursor.execute("SELECT store_id FROM store")
        rows = cursor.fetchall()

        for row in rows :
            if store_id == row[0] :
                return render_template("order.html")
    return render_template("order.html")

if __name__ == "__main__":
    app.run(debug=True)

