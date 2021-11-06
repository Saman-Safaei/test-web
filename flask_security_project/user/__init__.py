from flask import Blueprint


user_bp = Blueprint('users', __name__, url_prefix='/user/')


from . import models
from . import forms
from . import controllers
from . import admin
from . import views
from . import urls
