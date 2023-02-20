from flask_wtf import FlaskForm
import wtforms as f
from wtforms.validators import DataRequired


class CompanyForm(FlaskForm):
    name = f.StringField('name', validators=[DataRequired()])
    nip = f.IntegerField('nip', validators=[DataRequired()])

    display = ['name', 'nip']


class BuyerForm(CompanyForm):
    pass


class SellerForm(CompanyForm):
    pass


class UserForm(FlaskForm):
    email = f.StringField('email', validators=[DataRequired()])
    password = f.PasswordField('password', validators=[DataRequired()])

    display = ['email', 'password']