from django.db import models


class PizzaFlavor(models.Model):
    flavor = models.ForeignKey('Flavor', on_delete=models.PROTECT)
    pizza = models.ForeignKey('Pizza', on_delete=models.PROTECT)


class Pizza(models.Model):
    size = (
        (30, 'small 30cm'), (50, 'medium 50cm')
    )

    status = (
        (1, "Processing"),
        (2, "On the way"),
        (3, "Delivered")
    )

    name = models.CharField(max_length=50)
    small_size_price = models.DecimalField(max_digits=8, decimal_places=2)
    med_size_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Flavor(models.Model):
    flavor_name = models.CharField(max_length=50)
    on_top_of = models.ManyToManyField('Pizza', through=PizzaFlavor)

    def __str__(self):
        return self.flavor_name
