from flask_security import SQLAlchemyUserDatastore
from flask_security.models import fsqla_v2
from flask_security_project.core.extensions import db

# Define Models
fsqla_v2.FsModels.set_db_info(db)


# Role Table
class Role(db.Model, fsqla_v2.FsRoleMixin):
    __tablename__ = 'role'


# User Table
class User(db.Model, fsqla_v2.FsUserMixin):
    __tablename__ = 'user'


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
