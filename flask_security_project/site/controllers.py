from flask.views import View
from flask import render_template, request


class CPage(View):

    _template_name = ""

    def render_template(self, data):
        return render_template(self.template_name, data=data)

    # Should Override This method for passing data in front-end
    def get_data(self) -> dict:
        return {
            "empty": True
        }

    # The Response
    def dispatch_request(self, **kwargs):
        return self.render_template(self.get_data())

    # Template-Name Property
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value: str):
        self._template_name = value

    # Active Page Property
    @property
    def active_page(self):
        return request.args.get('p', 1, type=int)


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
