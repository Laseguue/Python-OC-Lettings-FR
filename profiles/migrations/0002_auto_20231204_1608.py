# Generated by Django 3.0 on 2023-12-04 16:08

from django.db import migrations

def forwards(apps, schema_editor):
    try:
        OldProfile = apps.get_model("oc_lettings_site", "Profile")
    except LookupError:
        return

    NewProfile = apps.get_model("profiles", "Profile")

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            id=old_profile.id,
            favorite_city=old_profile.favorite_city,
            user=old_profile.user
        )

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
