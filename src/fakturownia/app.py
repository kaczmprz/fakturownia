from flask import Flask
from .database import db
from .views import blueprints


def create_app():
    app = Flask(__name__)
    app.config['WTF_CSRF_SECRET_KEY'] = 'A SECRET KEY'
    app.config['SECRET_KEY'] = 'ANOTHER ONE'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fakturownia.db'

    for bp in blueprints:
        app.register_blueprint(bp)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()