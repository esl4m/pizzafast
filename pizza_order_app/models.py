from django.db import models
from pizza_app.models import Pizza


class Order(models.Model):
    pizza = models.ForeignKey('pizza_app.Pizza', on_delete=models.PROTECT)
    size = models.IntegerField(choices=Pizza.size, default=30, blank=False)  # added small size as default
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField(null=False, blank=False)

    def price(self):
        if self.size == 30:
            return self.pizza.small_size_price

        if self.size == 50:
            return self.pizza.med_size_price

        return self.pizza.small_size_price  # for the default case
