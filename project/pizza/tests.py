from django.test import TestCase
from django.urls import reverse, resolve


class PizzaTestCase(TestCase):

    def setUp(self) -> None:
        pass

    def test_page_pizza_form_add(self):
        response = self.client.get('/pizza-form-add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form_pizza_add.html')

    def test_page_pizza_price_update(self):
        response = self.client.get('/pizza-price-update/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pizza_price_update.html')

    def test_page_pizza_edit(self):
        url = reverse('pizza_update', args=[135])
        used = resolve(url)
        self.assertEquals(url, '/pizza-update/135/edit/')
        self.assertEqual(used.view_name, 'pizza_update')

    def test_page_pizza_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pizza_home.html')
        self.assertContains(response, 'АМЕРИКАНО')

