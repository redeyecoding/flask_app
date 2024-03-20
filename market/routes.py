from market import app
from .models import Item
from flask import render_template
from market import db



@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market():
    items = Item.query.all()
    print(f'[items!!!!] {items}')
    return render_template('market.html', items=items)

