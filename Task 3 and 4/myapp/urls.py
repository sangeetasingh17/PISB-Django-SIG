from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("userhome/", views.userHome, name='userhome'),
    path("login/", views.userLogin, name='login'),
    path("logout/", views.userLogout, name='logout'),
    path("search/", views.search, name='search'),
]
