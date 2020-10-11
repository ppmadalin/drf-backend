from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", view=views.api_root),
    path("login/", view=views.LoginView.as_view(), name="login"),
    path("users/", view=views.UserView.as_view(), name="user-list"),
    path("users/<int:pk>/", view=views.UserView.as_view(), name="user-detail"),
    path("posts/", view=views.PostView.as_view(), name="post-list"),
    path("posts/<int:pk>/", view=views.PostView.as_view(), name="post-detail"),
]
