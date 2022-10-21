from unittest import TestCase

from customers import views
from django.test import TestCase as DjangoTestCase
from django.urls import resolve, reverse


class TestCustomersUnittestTestCase(TestCase):
    def test_url_home_is_correct(self):
        url = reverse('customers:home')
        self.assertEqual('/', url)

    def test_url_home_loads_view_correct(self):
        response = resolve(reverse('customers:home'))
        self.assertEqual(response.func, views.home)


class TestCustomersDjangoTestCase(DjangoTestCase):
    def test_view_loads_template_is_correct(self):
        response = self.client.get(reverse('customers:home'))
        self.assertTemplateUsed(response, 'customers/pages/home.html')
