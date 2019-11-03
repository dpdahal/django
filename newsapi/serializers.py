from rest_framework import serializers

from news.models import Product


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
