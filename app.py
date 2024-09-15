from flask import Flask

from data import database as db


def create_app():
    app = Flask(__name__)
    
    
    # Initialize SQLAlchemy with the app
    app.config[db.SQLALCHEMY_DATABASE_URI] = db.SQL_ALCHEMY_CONFIGS[db.SQLALCHEMY_DATABASE_URI]
    app.config[db.SQLALCHEMY_TRACK_MODIFICATIONS] = db.SQL_ALCHEMY_CONFIGS[db.SQLALCHEMY_TRACK_MODIFICATIONS]
    db.INSTANCE.init_app(app)
    
    # Import models and create tables
    with app.app_context():
        from data.models import User
        db.INSTANCE.create_all()
    
    return app

app = create_app()

@app.route("/")
def hello_world():
    return "<p>Hello, Världen!</p>"
