# Generated by Django 3.2.16 on 2023-01-30 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0018_privateregister_update_volunteerusers'),
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
