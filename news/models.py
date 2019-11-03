from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = 'Category'


class Product(models.Model):
    posted_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(blank=True, upload_to='product')
    status = models.BooleanField(default=0)
    description = RichTextField()

    class Meta:
        verbose_name_plural = 'product'


class Slider(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(blank=True, upload_to='slider')
    status = models.BooleanField(default=0)
    description = RichTextField()

    def __str__(self):
        return self.title
