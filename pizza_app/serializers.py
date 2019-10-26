from rest_framework import serializers
from .models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'small_size_price', 'med_size_price')


class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'flavor_name', 'on_top_of')


class PizzaFlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'flavor', 'pizza')
