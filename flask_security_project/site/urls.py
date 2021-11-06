from . import site_bp, views

site_bp.add_url_rule('/', view_func=views.VIndex.as_view('index'))
site_bp.add_url_rule('/category/<string:category>', view_func=views.VCategoryList.as_view('category'))
site_bp.add_url_rule('/post/<int:post_id>', view_func=views.VSinglePost.as_view('post'))
site_bp.add_url_rule('/uploads/<string:filename>', view_func=views.VUploads.as_view('uploads'))
site_bp.add_url_rule('/search', view_func=views.VSearchList.as_view('search'))
