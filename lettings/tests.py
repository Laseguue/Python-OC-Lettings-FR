from django.test import TestCase, override_settings
from .models import Address, Letting
from unittest.mock import patch
from django.urls import reverse, resolve
from .views import index, letting


class AddressModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123, street="Main Street", city="Anytown", state="NY",
            zip_code=10001, country_iso_code="USA"
        )

    def test_address_creation(self):
        self.assertTrue(isinstance(self.address, Address))
        self.assertEqual(self.address.__str__(), '123 Main Street')


class LettingModelTest(TestCase):
    def setUp(self):
        address = Address.objects.create(
            number=123, street="Main Street", city="Anytown", state="NY",
            zip_code=10001, country_iso_code="USA"
        )
        self.letting = Letting.objects.create(
            title="Test Letting", address=address
        )

    def test_letting_creation(self):
        self.assertTrue(isinstance(self.letting, Letting))
        self.assertEqual(self.letting.__str__(), 'Test Letting')


class LettingsViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        address = Address.objects.create(
            number=123, street="Main Street", city="Anytown",
            state="NY", zip_code=10001, country_iso_code="USA"
        )
        Letting.objects.create(title="Test Letting", address=address)

    def test_index_view(self):
        response = self.client.get(reverse('lettings:index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_view(self):
        letting_id = Letting.objects.get(title="Test Letting").id
        response = self.client.get(
            reverse('lettings:letting', args=[letting_id]), follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')


@override_settings(DEBUG=False)
class LettingsViewsExceptionTest(TestCase):
    @patch('lettings.models.Letting.objects.all')
    def test_index_view_exception(self, mock_lettings_all):
        mock_lettings_all.side_effect = Exception("Test exception")

        with self.assertRaises(Exception):
            self.client.get(reverse('lettings:index'), follow=True)

    @classmethod
    def setUpTestData(cls):
        address = Address.objects.create(
            number=123, street="Main Street", city="Anytown",
            state="NY", zip_code=10001, country_iso_code="USA"
        )
        cls.letting = Letting.objects.create(
            title="Test Letting", address=address
        )

    def test_letting_view_http404_exception(self):
        non_existent_id = self.letting.id + 1
        response = self.client.get(
            reverse('lettings:letting', args=[non_existent_id]), follow=True
        )

        self.assertEqual(response.status_code, 404)

    @patch('lettings.views.get_object_or_404')
    def test_letting_view_general_exception(self, mock_get_object_or_404):
        mock_get_object_or_404.side_effect = Exception("Test exception")

        with self.assertRaises(Exception):
            self.client.get(
                reverse('lettings:letting', args=[self.letting.id]), follow=True
            )


class LettingsURLsTest(TestCase):
    def test_index_url(self):
        url = reverse('lettings:index')
        self.assertEqual(resolve(url).func, index)

    def test_letting_url(self):
        url = reverse('lettings:letting', args=[1])
        self.assertEqual(resolve(url).func, letting)
