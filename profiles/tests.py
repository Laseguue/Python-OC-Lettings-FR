from django.urls import reverse, resolve
from django.test import TestCase, override_settings
from unittest.mock import patch
from django.contrib.auth.models import User
from .views import index, profile
from .models import Profile


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='12345')
        Profile.objects.create(user=user, favorite_city="Paris")

    def test_profile_creation(self):
        user = User.objects.get(username='testuser')
        profile = Profile.objects.get(user=user)
        self.assertTrue(isinstance(profile, Profile))
        self.assertEqual(profile.favorite_city, "Paris")

    def test_profile_str(self):
        user = User.objects.get(username='testuser')
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.__str__(), user.username)


class ProfilesViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='12345')
        Profile.objects.create(user=user, favorite_city="Paris")

    def test_index_view(self):
        response = self.client.get(reverse('profiles:index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_view(self):
        user = User.objects.get(username='testuser')
        response = self.client.get(
            reverse('profiles:profile', args=[user.username]), follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')


@override_settings(DEBUG=False)
class ProfilesViewsExceptionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='12345')
        Profile.objects.create(user=user, favorite_city="Paris")

    @patch('profiles.models.Profile.objects.all')
    def test_index_view_exception(self, mock_profiles_all):
        mock_profiles_all.side_effect = Exception("Test exception")

        with self.assertRaises(Exception):
            self.client.get(reverse('profiles:index'), follow=True)

    def test_profile_view_http404_exception(self):
        response = self.client.get(
            reverse('profiles:profile', args=['nonexistentuser']), follow=True
        )

        self.assertEqual(response.status_code, 404)

    @patch('profiles.views.get_object_or_404')
    def test_profile_view_general_exception(self, mock_get_object_or_404):
        mock_get_object_or_404.side_effect = Exception("Test exception")

        with self.assertRaises(Exception):
            self.client.get(reverse('profiles:profile', args=['testuser']), follow=True)


class ProfilesURLsTest(TestCase):
    def test_index_url(self):
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, index)

    def test_profile_url(self):
        url = reverse('profiles:profile', args=['testuser'])
        self.assertEqual(resolve(url).func, profile)
