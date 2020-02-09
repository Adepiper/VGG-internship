from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from VGGchallenge.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)

    ENV = 'prod'

    if ENV == 'dev' : 
        app.debug = True
        app.config.from_object(Config)
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Adeola2009.@localhost/VggInternship'
    else :
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vvtotfjyntpcaf:94b0960541c95c579ee2b6167bce87e5390397cd051a49888aa60a6d55f4b77f@ec2-3-234-109-123.compute-1.amazonaws.com:5432/d48mi4tt17c84'
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from VGGchallenge.users.routes import users
    from VGGchallenge.projects.routes import projects
    from VGGchallenge.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(projects)
    app.register_blueprint(main)

    return app

    
