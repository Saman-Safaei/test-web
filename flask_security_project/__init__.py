from flask_security_project.core import Application
from flask_security_project.core import settings
from flask_security_project.core.extensions import security
from flask_security_project.core.extensions import db
from flask_security_project.core.extensions import mail
from flask_security_project.core.extensions import admin
from flask_security_project.core.extensions import login_manager
from flask_security_project.user.models import user_datastore


def create_app():
    # an instance of the Flask (Application)
    app = Application(
        __name__,
        template_folder=settings.templates_path,
        static_folder=settings.static_path
    )

    # Load Configuration
    app . config . from_pyfile(settings.__file__)

    # Register Blueprints
    app.install_blueprints()

    # Initialize Database
    app.install_database()

    # Initialize Error Pages - Like 404 Error and etc...
    app.install_error_handlers()

    # Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)
    security.init_app(app, datastore=user_datastore)
    admin.init_app(app)
    mail.init_app(app)

    # print(app.config["SECURITY_MSG_INVALID_EMAIL_ADDRESS"])

    return app


