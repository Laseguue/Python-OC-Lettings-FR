from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile in the system.

    This model extends the default User model by adding additional
    user-specific information.
    Each Profile is associated with one User instance. The Profile model
    includes a field for
    the user's favorite city. The CASCADE delete rule ensures that the profile
    is deleted
    when the associated User instance is deleted.

    Attributes:
        user (OneToOneField): A one-to-one link to Django's User model.
        It establishes a relationship
                              where each user has exactly one profile, and
                              each profile is associated
                              with exactly one user.
        favorite_city (CharField): A field to store the user's favorite city.
        This field is optional.

    Methods:
        __str__: Returns the username of the associated User instance.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the Profile, which is the username
        of the associated user.
        """
        return self.user.username
