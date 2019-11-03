from django.shortcuts import render

from .serializers import NewsSerializer

from news.models import Product
from rest_framework import viewsets


# Create your views here.

class NewsApiDetails(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = NewsSerializer
