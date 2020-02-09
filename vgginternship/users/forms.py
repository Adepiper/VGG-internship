from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo ,ValidationError
from VGGchallenge.models import User



class registerForm(FlaskForm):
    username = StringField('username', 
                validators=[DataRequired(),
                    Length(min=2, max=15)])

    password = PasswordField('Password', validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')


    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user: 
            raise ValidationError('Username is taken. Try another')

class loginForm(FlaskForm):
    username = StringField('username', 
                validators=[DataRequired(),
                    Length(min=2, max=15)])


    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

class updateAccountForm(FlaskForm):
    username = StringField('username', 
                validators=[DataRequired(),
                    Length(min=2, max=15)])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if  username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user: 
                raise ValidationError('Username is taken. Try another')

