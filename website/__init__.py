from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate  # Import Flask-Migrate for database migrations

# Database and app initialization
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To avoid warnings
    
    db.init_app(app)

    # Register blueprints for views and auth
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Initialize the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        from .models import User
        return User.query.get(int(id))
    migrate = Migrate(app, db)

    create_database(app)

    return app


def create_database(app):
    """This function checks if the database exists and creates it if necessary."""
    if not path.exists('website/' + DB_NAME):  # If the database file doesn't exist
        with app.app_context():  # Make sure to use app context when creating the DB
            db.create_all()  # Create all tables
        print('Created Database!')
    else:
        print("Database already exists, skipping creation.")
