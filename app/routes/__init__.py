from flask import Blueprint

main = Blueprint('routes', __name__)

from . import errors, views