from flask import Blueprint, render_template, request, redirect

from ..database import db, Buyer
from ..forms import BuyerForm

buyer = Blueprint('buyer', __name__, url_prefix='/buyers')


@buyer.route('/')
def index():
    buyers = db.session.query(Buyer)
    return render_template("buyers.html", buyers=buyers)


@buyer.route('/create_buyer', methods=['GET', 'POST'])
def create_buyer():
    form = BuyerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_buyer = Buyer()
            form.populate_obj(new_buyer)
            db.session.add(new_buyer)
            db.session.commit()
            return redirect('/buyers')

    return render_template("create_buyer.html", form=form)