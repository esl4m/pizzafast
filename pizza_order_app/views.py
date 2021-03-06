from rest_framework import generics
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class GetOrderByCustomer(generics.ListAPIView):
    """
    GET: Get list of all orders by customer name.
    """
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self):
        customer = self.kwargs['customer']
        queryset = self.model.objects.filter(customer_name=customer)
        if queryset:
            return queryset


class GetOrderByStatus(generics.ListAPIView):
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self):
        status = self.kwargs['status']
        queryset = self.model.objects.filter(status=status)
        print(queryset)
        if queryset:
            return queryset
