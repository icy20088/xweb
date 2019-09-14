from flask import Blueprint

main_bp = Blueprint('routes', __name__)

from . import errors, views