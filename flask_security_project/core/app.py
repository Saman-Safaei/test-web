from flask import Flask


class Application(Flask):

    _app = None

    def __new__(cls, *args, **kwargs):
        if cls._app is None:
            cls._app = super().__new__(cls)
        return cls._app

    def install_blueprints(self):
        from flask_security_project.user import user_bp
        from flask_security_project.site import site_bp

        self.register_blueprint(user_bp)
        self.register_blueprint(site_bp)

    def install_database(self):
        from . import database_initializer

    def install_error_handlers(self):
        from . import exceptions

    @classmethod
    def get_app(cls) -> Flask:
        return cls._app
