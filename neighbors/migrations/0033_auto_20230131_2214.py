# Generated by Django 3.2.16 on 2023-01-31 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0032_privateregister_update_volunteerusers'),
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
