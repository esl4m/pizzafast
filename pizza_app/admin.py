from django.contrib import admin
from .models import Pizza, Flavor, PizzaFlavor


admin.site.register(Pizza)
admin.site.register(Flavor)
admin.site.register(PizzaFlavor)
