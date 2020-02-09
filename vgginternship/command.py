import click
from flask.cli import with_appcontext

from vgginternship import db
from vgginternship.models import User, Projects, Actions

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()