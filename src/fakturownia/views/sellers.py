from flask import Blueprint, render_template, jsonify

from ..database import db, Seller

seller = Blueprint('seller', __name__, url_prefix='/sellers')


@seller.route('/')
def index():
    return jsonify({'Hello': 'sellers'})