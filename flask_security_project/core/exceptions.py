from flask import render_template

from . import Application


@Application.get_app().errorhandler(404)
def error_404(error):
    return render_template("error/error_404.html"), 404
