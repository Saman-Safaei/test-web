from flask.views import View
from flask import render_template
from . import forms


class CPage(View):
    _create_post_form = None
    _template_name = ""

    def render_template(self, data):
        return render_template(self.template_name, data=data)

    def get_data(self) -> dict:
        return {
            "empty": True
        }

    def dispatch_request(self, **kwargs):
        return self.render_template(self.get_data())

    # The Template-Name Property
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value: str):
        if type(value) is str:
            self._template_name = value
        else:
            raise TypeError("template-name must be 'String'")

    # The Create Post Form
    @property
    def create_post_form(self):
        if self._create_post_form is None:
            self._create_post_form = forms.FCreatePost()
        return self._create_post_form

# ----------------------------------------------------------------------------------------------------------------------
