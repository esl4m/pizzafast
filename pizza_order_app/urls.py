from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('order', views.OrderView)  # order is the endpoint

urlpatterns = [
    path('', include(router.urls)),
    path('order/create/', views.OrderCreate.as_view(), name='create'),
    path('order/edit/<int:pk>/', views.OrderEdit.as_view(), name='edit'),
    path('order/list/<customer>/', views.GetOrderByCustomer.as_view(), name='list'),
]
