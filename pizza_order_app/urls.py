from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('order', views.OrderView)  # order is the endpoint

urlpatterns = [
    path('', include(router.urls)),
    path('order/filter/customer/<customer>/', views.GetOrderByCustomer.as_view(), name='filter_by_customer'),
    path('order/filter/status/<status>/', views.GetOrderByStatus.as_view(), name='filter_by_status'),
]
