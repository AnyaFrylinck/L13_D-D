# #imports
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)

#     app.config['SECRET_KEY']= 'secret-key-goes-here'
#     app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.sqlite'

#     db.init_app(app)

#     # blueprints for auth
#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)

#     # non-auth blueprints
#     from .routes import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     return app
