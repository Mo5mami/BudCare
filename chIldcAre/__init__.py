from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from chIldcAre.config import Config
from flask_caching import Cache
from flask_mail import Mail



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
cache = Cache(config={'CACHE_TYPE': 'simple'})
mail=Mail()

@login_manager.user_loader
def load_user(user_id):
    return None

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    cache.init_app(app)
    mail.init_app(app)

    from chIldcAre.main.routes import main
    app.register_blueprint(main)
    from chIldcAre.users.routes import users
    app.register_blueprint(users)
    from chIldcAre.ml.routes import ml
    app.register_blueprint(ml)

    @app.context_processor
    def inject_enumerate():
        return dict(enumerate=enumerate)

    return app
