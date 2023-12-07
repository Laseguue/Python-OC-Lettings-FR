from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address in the system.

    This model stores information about an address, including its number,
    street, city, state, zip code,
    and country ISO code. It ensures that the state and country ISO code have
    a minimum length and the
    number and zip code do not exceed their maximum values.

    Attributes:
        number (PositiveIntegerField): The number of the address, must not
        exceed 9999.
        street (CharField): The street name, with a maximum length of 64
        characters.
        city (CharField): The city name, with a maximum length of 64
        characters.
        state (CharField): The state code, with a fixed length of 2 characters.
        zip_code (PositiveIntegerField): The zip code, must not exceed 99999.
        country_iso_code (CharField): The ISO country code, with a fixed
        length of 3 characters.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns a string representation of the address, combining the number
        and street.
        """
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a letting in the system.

    This model is used to store information about a letting, including its
    title and associated address.
    Each letting is linked to one unique address. When a letting is deleted,
    its associated address is
    also deleted due to the CASCADE delete rule.

    Attributes:
        title (CharField): The title of the letting, with a maximum length of
        256 characters.
        address (OneToOneField): A one-to-one link to an Address instance,
        with CASCADE delete behavior.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the title of the letting.
        """
        return self.title
