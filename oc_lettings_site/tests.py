from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib import admin
from oc_lettings_site import views as main_views


class MainIndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class MainURLsTest(TestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, main_views.index)

    def test_admin_url(self):
        url = reverse('admin:index')
        self.assertTrue(resolve(url).func.__name__, admin.site.urls)

    def test_lettings_url_inclusion(self):
        response = self.client.get('/lettings/')
        self.assertEqual(response.status_code, 200)

    def test_profiles_url_inclusion(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
