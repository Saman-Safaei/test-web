from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_security import current_user
from flask import redirect, url_for
from . import models
from flask_security_project.core import extensions


class PostModelView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and current_user.has_role('admin'))

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('security.login'))


extensions.admin.add_view(PostModelView(models.Post, extensions.db.session))
