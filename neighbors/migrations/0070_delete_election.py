# Generated by Django 3.2.16 on 2023-02-20 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0069_alter_election_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Election',
        ),
    ]