"""happy URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('404/', views.xfound, name='xFound'),
    path('categories-grid/', views.categoGrid, name='categoGrid'),
    path('categories-list/', views.categoList, name='categoList'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('single-post/', views.singlePost, name='singlePost'),
    path('typography/', views.typography, name='typography'),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
