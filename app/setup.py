import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .utils import safe_url, human_readable_format, human_readable_money_format, human_readable_percentage_format

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(name=__name__):
    """Create and configure the Flask app."""
    from .config import Config

    # Determine app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))

    app = Flask(
        name,
        static_folder=os.path.join(app_dir, 'static'),
        static_url_path='/static',
        template_folder=os.path.join(app_dir, 'templates')
    )

    # Configuration
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Set login view
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    # Register Blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register utilities in templates
    app.jinja_env.globals.update(
        safe_url=safe_url,
        human_readable_format=human_readable_format,
        human_readable_money_format=human_readable_money_format,
        human_readable_percentage_format=human_readable_percentage_format
    )

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    return app
