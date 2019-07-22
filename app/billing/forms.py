from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class CreateBillingForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired()])
    description = StringField('Description',
                              validators=[DataRequired()])
    value = DecimalField('Value',
                         validators=[DataRequired(), NumberRange(0)],
                         places=2)
    work_date = DateTimeField('Work Date',
                              validators=[DataRequired()])
    submit = SubmitField('Save')
