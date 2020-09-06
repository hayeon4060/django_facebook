"""facebooksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from face.views import play, play2
from face.views import my_profile
from face.views import event
from face.views import fail
from face.views import help
from face.views import warn
from face.views import newsfeed
from face.views import detail_feed
from face.views import pages
from face.views import new_feed
from face.views import new_page
from face.views import remove_feed, edit_feed
from face.views import remove_page, edit_page
urlpatterns = [
    path('admin/', admin.site.urls),

    path('play/', play),
    path('play2/', play2),
    path('dogeunchoi/profile/', my_profile),
    path('event/', event),
    path('fail/', fail),
    path('help/', help),
    path('warn/', warn),

    path('', newsfeed),
    path('feed/<pk>/', detail_feed),
    path('feed/<pk>/remove/', remove_feed),
    path('feed/<pk>/edit/', edit_feed),
    
    path('pages/<pk>/remove/', remove_page),
    path('pages/<pk>/edit/', edit_page),
   

    path('pages/', pages),
    path('pages/new/', new_page),
    

]
