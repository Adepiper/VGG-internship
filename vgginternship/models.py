from vgginternship.extensions import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True, nullable = False)
    password = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False, unique= True)
    description = db.Column(db.Text, nullable= False)
   # completed = db.Column(db.Boolean, default=False, nullable=True)
    actions = db.relationship('Actions', backref='project', lazy=True)

    def __repr__(self):
        return f"Projects('{self.name}', '{self.description}')"
    

class Actions (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable = False)
    description = db.Column(db.Text, nullable= False)
    note = db.Column(db.Text, nullable =False)

    def __repr__(self):
        return f"Actions('{self.project_id}', '{self.description}','{self.note}')"
