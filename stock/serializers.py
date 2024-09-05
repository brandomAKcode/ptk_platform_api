from rest_framework import serializers
from .models import ProductInStock, Rotation, ProductInRotation

class ProductInStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInStock
        fields = '__all__'
        
class RotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rotation
        fields = '__all__'
        
class ProductInRotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInRotation
        fields = '__all__'
    