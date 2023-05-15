"""GYM_SCHEDULER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include 
from django.urls import path
from HOME import urls as home_urls
from scheduler import urls as schedule_urls
# for static cacheing issues
from django.conf.urls.static import static

from django.contrib.staticfiles.views import serve

from django.views.decorators.cache import never_cache

from . import settings
urlpatterns = [
    path("admin/",admin.site.urls),
    path('',include(home_urls)),
]
if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, view=never_cache(serve))