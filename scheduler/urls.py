from django.urls import path
from . import views

urlpatterns = [
    path("",views.userpage,name="userpage"),
    path("newworkout/",views.newworkout,name="newworkout"),
    path("viewworkout/",views.viewworkout,name="viewworkout"),
    path("calculator/",views.calculator,name="calculator"),
    path("logout/",views.logout_user,name="logout")
    #  path("userpage/",views.userpage,name="userpage"),
]