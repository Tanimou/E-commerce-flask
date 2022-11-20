# This function is responsible for creating the username field
# The username field has a minimum length of 2 and a maximum length of 30
# The username field is validated using the DataRequired() and Length() validators
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from market.models import User
from market import bcrypt
def create_username_field():
    return StringField('User Name',validators=[Length(min=2,max=30),DataRequired()])

# This function is responsible for creating the email field
# The email field is validated using the DataRequired() and Email() validators
def create_email_field():
    return StringField('Email',validators=[DataRequired(),Email()])

# This function is responsible for creating the password field
# The password field is validated using the DataRequired() and Length() validators
def create_password_field():
    return PasswordField('Password',validators=[DataRequired(),Length(min=6)])

# This function is responsible for creating the confirm password field
# The confirm password field is validated using the DataRequired() and EqualTo() validators
def create_confirm_password_field():
    return PasswordField('Confirm password',validators=[EqualTo('password'),DataRequired()])

# This function is responsible for creating the submit button
def create_submit_button():
    return SubmitField('Register')
    
# This function is responsible for creating the registration form
# The form contains a username, email, password and confirm password fields
# The form also has a submit button
# The form is created using the FlaskForm class

# Creating the registration form
class RegisterForm(FlaskForm):
        username = create_username_field()
        email = create_email_field()
        password = create_password_field()
        confirm_password = create_confirm_password_field()
        submit = create_submit_button()

    #create a method that check if a user already exists in the database
    #if the user exists, the method will flash an error message to the user
    #if the user does not exist, the method will add the user to the database
        def validate_username(self,username_to_check):
            if user := User.query.filter_by(username=username_to_check.data).first():
                raise ValidationError('Username already exists! Please try a different username.')

        def validate_email_address(self,email_address_to_check):
            if email_address := User.query.filter_by(email_address=email_address_to_check.data).first():
                raise ValidationError('Email address already exists! Please try a different email address.')
            
    #create a class called LoginForm that inherits from the FlaskForm class
    #the LoginForm class will have a username and password field
    #the LoginForm class will also have a submit button
    #the username field will be validated using the DataRequired() validators
    #the password field will be validated using the DataRequired() validators
    #the submit button will be validated using the SubmitField() validators
    #the LoginForm class will also have a method called validate_username that will check if the username exists in the database
    #the LoginForm class will also have a method called validate_password that will check if the password is correct
class LoginForm(FlaskForm):
        username = StringField(label='User Name',validators=[DataRequired()])
        password = PasswordField(label='Password',validators=[DataRequired()])
        submit = SubmitField(label='Sign In')

        # def validate_username(self,username_to_check):
        #     user = User.query.filter_by(username=username_to_check.data).first()
        #     if not user:
        #         raise ValidationError('That username does not exist, please try again.')

        # def validate_password(self,password_to_check):
        #     if user := User.query.filter_by(username=self.username.data).first():
        #         if not self.check_password_correction(attempted_password=password_to_check.data):
        #             raise ValidationError('Password incorrect, please try again.')
                
    