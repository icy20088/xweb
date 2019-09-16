from flask import render_template, url_for
from . import main_bp
from app import db
from app.models.user import User
import os


@main_bp.route('/')
def index():
    images = os.listdir('app/static/image')
    return render_template('index.html', images = images)


@main_bp.route('/get/<string:image>')
def display(image):  
    return render_template('image.html', image = image)


@main_bp.route('/set/')
def produce():    
    wei = User(id=2, name='wei', age=27)
    db.session.add(wei)
    db.session.commit()
    return 'ok'


