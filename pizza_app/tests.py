from django.test import TestCase, Client
from .models import Pizza


class PizzaTest(TestCase):
    """ Test module for Pizza model """

    def setUp(self):
        self.pizza_url = '/api/pizza/'
        self.client = Client()

        self.name = 'Margarita'

        Pizza.objects.create(
            name='Margarita', small_size_price=10, med_size_price=15)


    def test_get_all_pizza(self):
        response = self.client.get(self.pizza_url)
        self.assertEqual(response.status_code, 200)  # response 200 .
