# Generated by Django 3.2.16 on 2023-02-26 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0087_rename_username_volunteerusers_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteerusers',
            old_name='inestagram_url',
            new_name='instagram_url',
        ),
    ]
