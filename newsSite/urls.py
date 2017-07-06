from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"index", views.welcome),
    url(r"login", views.publisher_login),
    url(r"register",views.publisher_register)
]
