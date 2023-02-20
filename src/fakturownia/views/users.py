from flask import Blueprint, request, render_template, redirect
from ..database import db, User
from ..forms import UserForm

user = Blueprint('user', __name__, url_prefix='/users')


@user.route('/')
def index():
    users = db.session.query(User)
    return render_template("user.html", users=users)


@user.route('/create', methods=['GET', 'POST'])
def create():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User()
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/users')
    return render_template("create.html", form=form)
