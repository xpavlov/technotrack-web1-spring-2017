from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from .views import *

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^logout/$', logout, name = "logout"),
    url(r'^login/$', login, {'template_name' : "core/login.html"}, name = "login"),
]