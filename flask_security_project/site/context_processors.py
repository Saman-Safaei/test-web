from flask_security_project.core import settings
from . import forms
from . import site_bp
from . import models


@site_bp.context_processor
def create_last_posts():
    last_posts = models.Post.query.filter_by(verified=True).order_by(models.Post.datetime_modified.desc()).limit(
        settings.last_posts_limit).all()
    return dict(last_posts=last_posts)


@site_bp.context_processor
def create_search_form():
    search_form = forms.FSearch()
    return dict(search_form=search_form)
