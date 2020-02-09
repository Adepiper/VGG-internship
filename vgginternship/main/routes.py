from flask import render_template, url_for, flash,redirect, request, Blueprint

main = Blueprint('main', __name__)



@main.route('/')
@main.route('/home')
def home(): 
    return render_template('index.html')


