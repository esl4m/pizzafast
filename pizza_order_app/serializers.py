from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'pizza', 'pizza_flavor', 'size', 'status', 'customer_name', 'customer_address', 'price')
        extra_kwargs = {'size': {'required': True}}
