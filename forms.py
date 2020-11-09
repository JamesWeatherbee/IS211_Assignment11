from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import email_validator


class SubmitForm(FlaskForm):
    task = StringField('Task',
                       validators=[DataRequired(), Length(min=3, max=200)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    # PUT THE DROPDOWN MENU HERE
    priority = StringField('Priority',
                           validators=[DataRequired()])
    submit = SubmitField('Add Task')