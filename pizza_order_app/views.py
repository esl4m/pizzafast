from rest_framework import generics
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreate(generics.CreateAPIView):
    """
    POST : Create new order.
    """
    model = Order
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
            # else
            # Handle the exception -- return 'customer not found'


class OrderEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
