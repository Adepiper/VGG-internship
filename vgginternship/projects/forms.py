from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo ,ValidationError





class projectForm(FlaskForm):
    Projectname = StringField('Projectname', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    submit = SubmitField('Add new project')

class actionForm(FlaskForm):
    description = TextAreaField('description', validators=[DataRequired()])
    note = TextAreaField('note', validators=[DataRequired()])
    submit = SubmitField('Add')



