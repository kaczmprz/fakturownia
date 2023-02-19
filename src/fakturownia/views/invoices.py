from flask import Blueprint, render_template, jsonify

from ..database import db, Invoice

invoice = Blueprint('invoice', __name__, url_prefix='/invoices')


@invoice.route('/')
def index():
    return jsonify({'Hello': 'invoices'})