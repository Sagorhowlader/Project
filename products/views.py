from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import *


@login_required
def ProductListView(request):
    qs = Product.objects.all()

    context = {'qs': qs}

    return render(request, 'product/productlist.html', context)
