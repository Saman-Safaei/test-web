from flask_admin import AdminIndexView
from flask_security import current_user
from flask import redirect, url_for


class AdminIndexSecure(AdminIndexView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and current_user.has_role('admin'))

    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('security.login'))