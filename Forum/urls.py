from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("newpost/", views.newpost, name="newpost"),
    path("signin/", views.pleasesignin, name="signin"),
    path("logout/", views.logout_view, name="logout"),
    path("you_are_banned/", views.banned_view, name="banned"),
    path("viewpost/<int:pk>", views.viewpost, name="viewpost"),
    path("deletepost/<int:pk>", views.delete_post, name="delete_post"),
    path("deletecomment/<int:pk>", views.delete_comment, name="delete_comment"),
    path("search/", views.search_posts, name="search"),
]
