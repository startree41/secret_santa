from flask import Blueprint

bp = Blueprint('main', __name__)

from service.main import service