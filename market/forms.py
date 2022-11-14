from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class RegisterForm(FlaskForm):
    username = StringField('User Name',validators=[Length(min=2,max=30),DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=6)])
    confirm_password = PasswordField('Confirm password',validators=[EqualTo('password'),DataRequired()])
    submit = SubmitField('Register')
    