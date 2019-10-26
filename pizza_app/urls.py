from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('pizza', views.PizzaView)  # pizza is the endpoint

urlpatterns = [
    path('', include(router.urls))
]
