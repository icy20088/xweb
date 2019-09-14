from flask import render_template
from . import main_bp
from app import db
from app.models.user import User


@main_bp.route('/')
def index():    
    return render_template('index.html')