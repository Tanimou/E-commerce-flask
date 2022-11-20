from market import app
from market.models import Item,init_db,add_item,add_user,get_user
from flask import render_template,redirect,url_for,flash,get_flashed_messages
from market.forms import RegisterForm,LoginForm
from flask_login import login_user,logout_user,login_required,current_user

@app.route("/")
@app.route("/home")
def home_page():
#    db.create_all()
    return render_template("home.html")

@app.route("/market/<name>")
@app.route("/market")
def market_page():

    # init_db()
    # add_user('cisse','cisse@live.fr','cisse')
    # add_user('samba','samba@live.fr','samba')
    # add_user('moussa','moussa@live.fr','moussa')
    # add_item('laptop','123456789012',500,'this is a laptop',get_user('cisse').id)
    # add_item('phone','123456789013',300,'this is a phone',get_user('samba').id)
    # add_item('keyboard','123456789',200,'this is a keyboard',get_user('moussa').id)
    items=Item.query.all()

    return render_template("market.html",name=items)

#The code below is used to register a user
#It takes the form input from the register.html page and checks if it is valid
#If the form is valid, the new user is added to the database and the user is redirected to the market page
#If the form is not valid, an error message is flashed to the user

@app.route("/register",methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        add_user(form.username.data,form.email.data,form.password.data)
        flash("Account created successfully! You are now able to log in", category='success')

        return redirect(url_for('market_page'))
    #if there are no errors from the validations
    if form.errors != {}:
        #we want to flash each error message to the client side so that users can see it
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}',category='danger')
    return render_template("register.html",form=form)

# add a route for the login page
@app.route("/login",methods=['GET','POST'])
# add a function for the login page
#The function will take the form input from the login.html page and check if it is valid
#If the form is valid, the function checks if the user exists in the database
#If the user exists, the function checks if the password is correct
#If the password is correct, the user is redirected to the market page
#If the password is incorrect, an error message is flashed to the user
#If the user does not exist, an error message is flashed to the user
#If the form is not valid, an error message is flashed to the user

def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user=get_user(form.username.data)
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again',category='danger')
    #if there are no errors from the validations
    if form.errors != {}:
        #we want to flash each error message to the client side so that users can see it
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}',category='danger')
    return render_template("login.html",form=form)