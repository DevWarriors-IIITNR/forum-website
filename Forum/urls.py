from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("newpost/", views.newpost, name="newpost"),
    path("signin/", views.pleasesignin, name="signin"),
    path("logout/", views.logout_view, name="logout"),
]
