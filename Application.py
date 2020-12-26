'''
To run:
set FLASK_APP=Application.py
set FLASK_ENV=development
flask run --port=80

To quit: Ctrl + C (you might have to type this more than once)
'''


from flask import Flask, render_template, request
from markupsafe import escape
import json
from uuid import uuid4
import sqlite3

app = Flask(__name__)

@app.route("/")
@app.route('/<path:subpath>')
def landing_page(subpath = 'index.html'):
    return render_template(escape(subpath))

@app.route("/submit_order", methods=["POST"])
def submit_order():
    order = {'firstName': '',
               'lastName': '',
               'pizzas': [],
               'id': '',
               'status': ''}
    
    order['firstName'] = request.form.get("firstName")
    order['lastName'] = request.form.get("lastName")
    
    first_pizza = {'pizzaType1':request.form.get("pizzaType1"),
                    'pizzaSize1':request.form.get("pizzaSize1"),
                    'pizzaCount1':request.form.get("pizzaCount1")}
    second_pizza = {'pizzaType2':request.form.get("pizzaType2"),
                    'pizzaSize2':request.form.get("pizzaSize2"),
                    'pizzaCount2':request.form.get("pizzaCount2")}
    order['pizzas'].append(first_pizza)
    order['pizzas'].append(second_pizza)

    order['id'] = str(uuid4())
    order['status'] = 'confirmed'

    for i in range (3):
        print()
    
    print(json.dumps(order, indent=4))

    for i in range (3):
        print()


    # Connect to SQLite database and store order info
    with sqlite3.connect("database.db") as conn:
        
        # conn.execute('DROP TABLE IF EXISTS order_pizza')
        conn.execute('CREATE TABLE if not exists order_pizza (id TEXT, status TEXT, f_name TEXT, l_name TEXT, pizzas TEXT)')

        ID = order['id']
        status = order['status']
        f_name = order['firstName']
        l_name = order['lastName']
        pizzas = json.dumps(order['pizzas'])

        conn.execute("INSERT INTO order_pizza (id, status, f_name,l_name,pizzas) VALUES (?,?,?,?,?)",\
                    (ID, status, f_name, l_name, pizzas))
        # print(conn.execute("SELECT * FROM order_pizza").fetchone())
        conn.commit()

    return render_template('summary.html', order = order)


# Check order
@app.route("/check_order/<order_id>")
def check_order(order_id):
    order = {'firstName': '',
               'lastName': '',
               'pizzas': [],
               'id': '',
               'status': ''}

    with sqlite3.connect("database.db") as conn:
        all_data = conn.execute("SELECT id, status, f_name,l_name,pizzas  FROM order_pizza").fetchall()
        for data in all_data:
            if data[0] == order_id:
                order['id'] = data[0]
                order['status'] = data[1]
                order['firstName'] = data[2]
                order['lastName'] = data[3]
                order['pizzas'] = json.loads(data[4])
                return render_template('check_order.html', order = order)

    return "Order not found"

if __name__ == "__main__":
    app.run(debug=True)
