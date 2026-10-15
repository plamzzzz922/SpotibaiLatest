from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_page, name="login"),
    path("play/<int:pk>/", views.player, name="player"),
    path("account/", views.account, name="account"),
    path("about/", views.about, name="about"),
    path("playlists/", views.playlists, name="playlists"),
    path("playlists/<int:pk>/", views.playlist, name="playlist"),
    path("liked/", views.liked, name="liked"),
    path("recent/", views.recent, name="recent"),
    path("trending/", views.trending, name="trending"),
]
