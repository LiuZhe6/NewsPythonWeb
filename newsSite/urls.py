from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"index", views.welcome),
    url(r"publogin", views.publisher_login),
    url(r"pubregister", views.publisher_register),
    url(r'ajaxhandle', views.ajax_response),
    url(r'alterinfo', views.alter_info),
    url(r'publishnews', views.publish_news),

]
