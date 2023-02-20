from flask import Blueprint, render_template, request, redirect

from ..database import db, Seller
from ..forms import SellerForm

seller = Blueprint('seller', __name__, url_prefix='/sellers')


@seller.route('/')
def index():
    sellers = db.session.query(Seller)
    return render_template("sellers.html", sellers=sellers)


@seller.route('/create', methods=['GET', 'POST'])
def create_seller():
    form = SellerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_seller = Seller()
            form.populate_obj(new_seller)
            db.session.add(new_seller)
            db.session.commit()
            return redirect('/sellers')
    return render_template("create.html", form=form)

