from . import user_bp
from . import views

user_bp.add_url_rule('/', view_func=views.VDashboard.as_view('dashboard'))
user_bp.add_url_rule('/create_post', view_func=views.VCreatePost.as_view('create_post'))
user_bp.add_url_rule('/demo/<string:post_id>', view_func=views.VDemoView.as_view('demo_post'))
