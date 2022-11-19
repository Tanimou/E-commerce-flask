from market import app
from market.models import Item,init_db,add_item,add_user,get_user,get_item,get_all_users,get_all_items,delete_user
from flask import render_template,redirect,url_for,flash,get_flashed_messages
from market.forms import RegisterForm

@app.route("/")
@app.route("/home")
def home_page():
#    db.create_all()
    return render_template("home.html")

@app.route("/market/<name>")
@app.route("/market")
def market():

    init_db()
    add_user('cisse','cisse@live.fr','cisse')
    add_user('samba','samba@live.fr','samba')
    add_user('moussa','moussa@live.fr','moussa')
    add_item('laptop','123456789012',500,'this is a laptop',get_user('cisse').id)
    add_item('phone','123456789013',300,'this is a phone',get_user('samba').id)
    add_item('keyboard','123456789',200,'this is a keyboard',get_user('moussa').id)
    items=Item.query.all()

    return render_template("market.html",name=items)

#The code below is used to register a user
#It takes the form input from the register.html page and checks if it is valid
#If the form is valid, the new user is added to the database and the user is redirected to the market page
#If the form is not valid, an error message is flashed to the user

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        add_user(form.username.data,form.email.data,form.password.data)
        flash("Account created successfully! You are now able to log in", category='success')

        return redirect(url_for('market'))
    #if there are no errors from the validations
    if form.errors != {}:
        #we want to flash each error message to the client side so that users can see it
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}',category='danger')
    return render_template("register.html",form=form)