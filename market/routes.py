from market import app
from .models import Item, User
from flask import render_template, redirect, url_for, flash
from market import db
from market.forms import RegisterForm



@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', user_items=items)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    registration_form = RegisterForm()
    
    if registration_form.validate_on_submit():
        user_to_create = User(username=registration_form.username.data,
                              email_address=registration_form.email_address.data,
                              password_hash=registration_form.user_password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    
    if registration_form.errors != {}:
        for err_msgs in registration_form.errors.values():
            flash(f' ERROR CREATING USER! - {err_msgs}', category='danger')
    return render_template('register.html', reg_form=registration_form)