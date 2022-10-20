from unittest import TestCase

from customers import views
from django.urls import resolve, reverse


class TestCustomers(TestCase):
    def test_url_home_is_correct(self):
        url = reverse('customers:home')
        self.assertEqual('/', url)

    def test_url_home_loads_view_correct(self):
        response = resolve(reverse('customers:home'))
        self.assertEqual(response.func, views.home)
