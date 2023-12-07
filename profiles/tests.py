from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse, resolve
from .views import index, profile


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
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_view(self):
        user = User.objects.get(username='testuser')
        response = self.client.get(reverse('profiles:profile', args=[user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')


class ProfilesURLsTest(TestCase):
    def test_index_url(self):
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, index)

    def test_profile_url(self):
        url = reverse('profiles:profile', args=['testuser'])
        self.assertEqual(resolve(url).func, profile)
