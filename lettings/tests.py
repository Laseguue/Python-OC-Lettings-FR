from django.test import TestCase
from .models import Address, Letting
from django.urls import reverse, resolve
from .views import index, letting


class AddressModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123, street="Main Street", city="Anytown", state="NY", zip_code=10001, country_iso_code="USA")

    def test_address_creation(self):
        self.assertTrue(isinstance(self.address, Address))
        self.assertEqual(self.address.__str__(), '123 Main Street')


class LettingModelTest(TestCase):
    def setUp(self):
        address = Address.objects.create(
            number=123, street="Main Street", city="Anytown", state="NY", zip_code=10001, country_iso_code="USA")
        self.letting = Letting.objects.create(title="Test Letting", address=address)

    def test_letting_creation(self):
        self.assertTrue(isinstance(self.letting, Letting))
        self.assertEqual(self.letting.__str__(), 'Test Letting')


class LettingsViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        address = Address.objects.create(
            number=123, street="Main Street", city="Anytown", state="NY", zip_code=10001, country_iso_code="USA")
        Letting.objects.create(title="Test Letting", address=address)

    def test_index_view(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_view(self):
        letting_id = Letting.objects.get(title="Test Letting").id
        response = self.client.get(reverse('lettings:letting', args=[letting_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')


class LettingsURLsTest(TestCase):
    def test_index_url(self):
        url = reverse('lettings:index')
        self.assertEqual(resolve(url).func, index)

    def test_letting_url(self):
        url = reverse('lettings:letting', args=[1])
        self.assertEqual(resolve(url).func, letting)
