from .extensions import db
from .app import Application
from flask_security_project.user.models import user_datastore
from flask_security import hash_password


@Application.get_app().before_first_request
def bfr():
    db.create_all()
    if user_datastore.find_user(email='xsamansafaeix@gmail.com') is None:
        user = user_datastore.create_user(email='xsamansafaeix@gmail.com',
                                          username="admin",
                                          password=hash_password('admin123'))
        role = user_datastore.create_role(name="admin", permissions=['admin', 'full-control'])
        user_datastore.add_role_to_user(user, role)
        user_datastore.commit()
