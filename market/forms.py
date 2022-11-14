from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,PasswordField

class RegisterForm(FlaskForm):
    username = StringField('User Name')
    email = StringField('Email')
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm password')
    submit = SubmitField('Register')
    