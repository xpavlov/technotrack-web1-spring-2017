from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blogs_list"),
    url(r'^(?P<pk>\d+)$', BlogView.as_view(), name="one_blog"),
    url(r'^(?P<pk>\d+)/edit$', UpdateBlog.as_view(), name="edit_blog"),
    url(r'^add$', login_required(CreateBlog.as_view()), name="new_blog"),

    url(r'^post/(?P<pk>\d+)/edit$', login_required(UpdatePost.as_view()), name="edit_post"),
    url(r'^(?P<pk>\d+)/add$', login_required(CreatePost.as_view()), name="add_post"),

    url(r'^post/(?P<pk>\d+)$', PostDetail.as_view(), name="one_post"),
    url(r'^post/(?P<pk>\d+)/add_comment$', PostDetail.as_view(), name="detail_post"),
    url(r'^categories/$', CategoryList.as_view(), name="category_list"),
    url(r'^category/(?P<pk>\d+)$', CategoryView.as_view(), name="one_category"),
    url(r'^like/(?P<pk>\d+)$', PostLikeAjaxView.as_view(), name="post_ajax_like"),
    url(r'^likes/(?P<pk>\d+)$', BlogLikeView.as_view(), name="blog_likes")
]