from flask_security_project.core import settings
from flask import send_from_directory, request, render_template
from . import controllers
from . import models
from . import utilities
from . import forms


class VIndex(controllers.CPage):

    def get_data(self) -> dict:
        self.template_name = "site/list_view.html"

        posts_info = models.Post.query.order_by(
            models.Post.datetime_modified.desc()).filter_by(
            verified=True).paginate(
            page=self.active_page,
            per_page=settings.per_page)
        return {
            "posts_info": posts_info,
            "page_numbers": utilities.get_page_numbers(posts_info, self.active_page)
        }


# ----------------------------------------------------------------------------------------------------------------------


class VSearchList(controllers.CPage):
    methods = ["GET", "POST"]

    def get_data(self) -> dict:
        self.template_name = "site/list_view.html"
        self.search_data = "%" + request.form.get('search_field', "") + "%"
        posts_info = models.Post.query.order_by(
            models.Post.datetime_modified.desc()).filter_by(
            verified=True).filter(
            models.Post.title.like(self.search_data) | models.Post.short_body_text.like(self.search_data)).paginate(
            page=self.active_page,
            per_page=settings.per_page)
        return {
            "posts_info": posts_info,
            "page_numbers": utilities.get_page_numbers(posts_info, self.active_page)
        }


# ----------------------------------------------------------------------------------------------------------------------


class VCategoryList(controllers.CPage):

    def get_data(self) -> dict:
        self.template_name = "site/list_view.html"

        posts_info = models.Post.query.order_by(
            models.Post.datetime_modified.desc()).filter_by(
            verified=True, category=self.category).paginate(
            page=self.active_page,
            per_page=settings.per_page)
        return {
            'title': 'دسته بندی {0}'.format(self.category),
            "posts_info": posts_info,
            "page_numbers": utilities.get_page_numbers(posts_info, self.active_page)
        }

    def dispatch_request(self, **kwargs):
        self.category = kwargs.get('category', '')
        return self.render_template(self.get_data())


# ----------------------------------------------------------------------------------------------------------------------


class VSinglePost(controllers.CPage):

    def get_data(self) -> dict:
        self.template_name = "site/single_post.html"
        return {
            "post_info": models.Post.query.filter_by(_id=self.post_id, verified=True).first_or_404()
        }

    def dispatch_request(self, **kwargs):
        self.post_id = kwargs.get('post_id')
        return self.render_template(self.get_data())


# ----------------------------------------------------------------------------------------------------------------------


class VUploads(controllers.CPage):
    def dispatch_request(self, **kwargs):
        self.filename = kwargs.get('filename')
        return send_from_directory(settings.UPLOAD_FOLDER, settings.UPLOAD_FOLDER, filename=self.filename)
