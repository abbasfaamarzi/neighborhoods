# Generated by Django 3.2.16 on 2023-01-31 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0028_privateregister'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrivateRegister',
        ),
        migrations.DeleteModel(
            name='Update',
        ),
        migrations.DeleteModel(
            name='VolunteerUsers',
        ),
    ]