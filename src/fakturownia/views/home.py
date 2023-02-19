from flask import Blueprint, render_template, jsonify

from ..database import db

home = Blueprint('home', __name__)


@home.route('/')
def index():
    return jsonify({'Hello': 'world'})