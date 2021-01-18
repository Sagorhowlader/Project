from django.urls import path
from .views import *
urlpatterns = [
    path('', eventview,name='admin'),

]