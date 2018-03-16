from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed


class CiscoKeyboard(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    serialNumber = StringField('Serial Number', validators = [DataRequired()])
    functional = SelectField('Functional', choices = [('Descrption', 'Select Functionality'), ('Y', 'Yes'),
                                                      ('N', 'No')])
