from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("login/", views.login),
    path("me/", views.MeView.as_view()),
    path("me/favs", views.FavsView.as_view()),
    path("<int:pk>/", views.user_detail),
    path("<int:pk>/favs", views.UserFavsView.as_view())
]
