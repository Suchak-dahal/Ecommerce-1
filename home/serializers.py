# Serializers define the API representation.
from rest_framework import routers, serializers, viewsets
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['__all__']
