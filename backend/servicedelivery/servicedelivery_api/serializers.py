from rest_framework import serializers
from .models import Order, OrderItem, InstalledAsset

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class InstalledAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstalledAsset
        fields = '__all__'