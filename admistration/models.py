from django.db import models
from products.models import *


# Create your models here.

class Event(models.Model):
    event_id = models.CharField(max_length=50, blank=False)
    event_name = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='event/images', default="", null=True)
    product = models.ManyToManyField(Product, blank=True, related_name='product')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
