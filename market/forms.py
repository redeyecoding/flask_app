from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! You gotta try a different username!')
    
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('The email address you entered already exists! You gotta try a different email address!')
    
    username = StringField(label='User Name:', validators=[Length(min=4, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    user_password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password:', validators=[EqualTo('user_password'), DataRequired()])
    submit = SubmitField(label='Create Account')

