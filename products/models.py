from django.db import models

from django.db import models
from PIL import Image


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True, blank=False)
    product_name = models.CharField(max_length=200, blank=False)
    product_description = models.TextField(max_length=300, blank=True)
    category = models.ForeignKey(category, default="", verbose_name="Category", on_delete=models.SET_DEFAULT, null=True)
    image1 = models.ImageField(upload_to='products/images', default="", null=True)
    image2 = models.ImageField(upload_to='products/images', default="", null=True, blank=True)
    image3 = models.ImageField(upload_to='products/images', default="", null=True, blank=True)
    price = models.FloatField(default=0.0, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img1 = Image.open(self.image1.path)
        if img1.height > 1500 or img1.width > 1500:
            output_size = (1500, 1500)
            img1.thumbnail(output_size)
            img1.save(self.image1.path)
        if self.image2:
            img2 = Image.open(self.image2.path)
            if img2.height > 1500 or img2.width > 1500:
                output_size = (1500, 1500)
                img2.thumbnail(output_size)
                img2.save(self.image2.path)

        if self.image3:
            img3 = Image.open(self.image3.path)
            if img3.height > 1500 or img3.width > 1500:
                output_size = (1500, 1500)
                img3.thumbnail(output_size)
                img3.save(self.image3.path)

    def __str__(self):
        return f'{self.product_id}--{self.product_name}'

    def all_profuct_list(self):
        product = Product.objects.all()
        return product


class Advertisement(models.Model):
    name = models.CharField(max_length=50, blank=False)
    product = models.ManyToManyField(Product, verbose_name="Product", related_name='products')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'
