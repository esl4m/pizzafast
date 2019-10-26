from django.shortcuts import render
from rest_framework import viewsets
from .models import Pizza, Flavor, PizzaFlavor
from .serializers import PizzaSerializer, FlavorSerializer, PizzaFlavorSerializer


class PizzaView(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class FlavorView(viewsets.ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer


class PizzaFlavorView(viewsets.ModelViewSet):
    queryset = PizzaFlavor.objects.all()
    serializer_class = PizzaFlavorSerializer
