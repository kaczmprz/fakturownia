from flask_wtf import FlaskForm
import wtforms as f
from wtforms.validators import DataRequired


class BuyerForm(FlaskForm):
    name = f.StringField('name', validators=[DataRequired()])
    nip = f.IntegerField('nip', validators=[DataRequired()])

    display = ['name', 'nip']