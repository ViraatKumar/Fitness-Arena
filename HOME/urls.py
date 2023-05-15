from django.urls import path
from django.conf.urls import include 
from . import views
from scheduler import urls as user_links
urlpatterns=[
path("",views.homepage,name='homePage'),
# path("loginreg/<str:arg>/",views.loginreg,name="loginregargs"),
path("loginreg/",views.loginreg,name="loginreg"),
# path("home_view/",views.home_view,name="home"),
# path("register/",views.register,name="userPage"),
path("login/",views.login,name="loggedin"),
path("userpage/",include(user_links),name="userpage"),
path("homepage/",views.homepage,name="homepage")
]