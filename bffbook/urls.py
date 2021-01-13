"""bffbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import registerPage,login,logoutUser
import notifications.urls
admin.site.site_header="Admin Login"
admin.site.site_title="Admin | Dashboard"
admin.site.index_title="Welcome to admin panel"
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', login, name='login'),
    path('register/',registerPage,name='register'),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('product/', include('products.urls', namespace='product')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('login/',login,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('notifications/', include(notifications.urls, namespace='notifications')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
