from flask_security_project.core import Application


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Application.get_app().config.get('ALLOWED_FILES')
