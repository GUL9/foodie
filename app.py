from flask import Flask

from data import database as db
from data import models

_USER_API = models.get_api(models.DataModels.USER)



def create_app():
    app = Flask(__name__)
    
    
    # Initialize SQLAlchemy with the app
    app.config[db.SQLALCHEMY_DATABASE_URI] = db.SQL_ALCHEMY_CONFIGS[db.SQLALCHEMY_DATABASE_URI]
    app.config[db.SQLALCHEMY_TRACK_MODIFICATIONS] = db.SQL_ALCHEMY_CONFIGS[db.SQLALCHEMY_TRACK_MODIFICATIONS]
    db.INSTANCE.init_app(app)
    
    # Import models and create tables
    with app.app_context():
        from data.user import User
        db.INSTANCE.create_all()
        
    
    return app

app = create_app()

@app.route("/")
def hello_world():
    #_USER_API.create_new(username="anton")
    anton = _USER_API.get_by_username(username="anton")
    return f"<p>Hello, {anton.username}</p>"

