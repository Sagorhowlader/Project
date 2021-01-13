from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import *
from django.views.generic import DetailView

@login_required
def ProductListView(request):
    qs = Product.objects.all()

    context = {'qs': qs}

    return render(request, 'product/productlist.html', context)

class ProductProfileDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = ('product/details.html')

    def get_context_data(self, **kwargs):
        product_id=self.kwargs.get('pk')
        obj=Product.objects.get(product_id=product_id)
        context = {'qs': obj}
        return context

#
