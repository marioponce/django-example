from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="user_home"),
    path("login/", views.user_login, name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    path("cga/", views.view_cga, name="cga"),
    path("de/", views.view_de, name="de"),
]