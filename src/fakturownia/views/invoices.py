from flask import Blueprint, render_template

from ..database import db, Invoice

invoice = Blueprint('invoice', __name__, url_prefix='/invoices')


@invoice.route('/')
def index():
    invoices = db.session.query(Invoice)
    return render_template("invoices.html", invoices=invoices)