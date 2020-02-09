from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from vgginternship.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'e4b1815c5823da1786c3e1064793fec2'

    #ENV = 'prod'

    #if ENV == 'dev' : 
        #app.debug = True
        #app.config.from_object(Config)
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Adeola2009.@localhost/VggInternship'
    #else :
        #app.debug = False
       
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vvtotfjyntpcaf:94b0960541c95c579ee2b6167bce87e5390397cd051a49888aa60a6d55f4b77f@ec2-3-234-109-123.compute-1.amazonaws.com:5432/d48mi4tt17c84'
    ENV = 'prod'

    if ENV == 'dev' : 
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Adeola2009.@localhost/VggInternship'
    else :
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zgmtnblwwuddsg:6eb8ab5364742a428b3df2996d9a5fe33555762ac3f415597966c6a5fa20bced@ec2-52-203-160-194.compute-1.amazonaws.com:5432/da85u9e2mvite9'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    from vgginternship.users.routes import users
    from vgginternship.projects.routes import projects
    from vgginternship.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(projects)
    app.register_blueprint(main)

    return app

    
