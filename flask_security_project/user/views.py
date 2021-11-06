import datetime
import os.path
from flask import redirect, url_for, render_template
from flask_security import auth_required, current_user
from werkzeug.utils import secure_filename
from flask_security_project.core import extensions
from flask_security_project.core import settings
from flask_security_project.site.models import Post
from . import controllers
from . import utilities


class VDashboard(controllers.CPage):
    decorators = [auth_required(), ]

    def get_data(self) -> dict:
        self.template_name = "user/dashboard.html"

        return {
            "my_posts_verified": Post.query.filter_by(author=current_user.username, verified=True).all(),
            "my_posts_not_verified": Post.query.filter_by(author=current_user.username, verified=False).all()
        }


# ----------------------------------------------------------------------------------------------------------------------


class VCreatePost(controllers.CPage):
    decorators = [auth_required(), ]
    methods = ['GET', 'POST']

    def get_data(self) -> dict:
        self.template_name = "user/create_post.html"

        return {
            'form': self.create_post_form
        }

    def render_template(self, data):
        if self.create_post_form.validate_on_submit():
            post_title = self.create_post_form.title_field.data
            post_picture = self.create_post_form.picture_field.data
            post_picture_filename = None
            if post_picture and utilities.allowed_file(post_picture.filename):
                post_picture_filename = secure_filename(post_picture.filename)
                post_picture.save(os.path.join(settings.UPLOAD_FOLDER, post_picture_filename))
            author = current_user.username
            datetime_modified = datetime.datetime.now()
            category = self.create_post_form.categories.data
            short_body_text = self.create_post_form.short_body_text.data
            full_body_text = self.create_post_form.full_body_text.data
            post = Post(title=post_title, img_name=post_picture_filename, author=author,
                        datetime_modified=datetime_modified, category=category,
                        short_body_text=short_body_text, full_body_text=full_body_text)
            extensions.db.session.add(post)
            extensions.db.session.commit()
            return redirect(url_for('users.dashboard'))
        return render_template(self.template_name, data=data)


# ----------------------------------------------------------------------------------------------------------------------


class VDemoView(controllers.CPage):
    decorators = [auth_required(), ]

    def get_data(self) -> dict:
        self.template_name = "user/demo_post.html"

        return {
            'post_info': Post.query.filter_by(_id=self.post_id, author=current_user.username).first_or_404(),
            'last_posts': Post.query.filter_by(verified=True).order_by(Post.datetime_modified.desc()).limit(
                settings.last_posts_limit).all()
        }

    def dispatch_request(self, **kwargs):
        self.post_id = kwargs.get('post_id')
        return self.render_template(self.get_data())
