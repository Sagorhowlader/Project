from django.urls import path, re_path
from .views import *
app_name = 'product'

urlpatterns = [
    path('', ProductListView, name='productlist'),

    ]