from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_admin import Admin
from flask_mail import Mail
from . import admin_secure


db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
security = Security()
admin = Admin(name='FlaskFa', template_mode='bootstrap4', index_view=admin_secure.AdminIndexSecure())
