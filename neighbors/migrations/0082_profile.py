# Generated by Django 3.2.16 on 2023-02-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0081_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('vb', models.IntegerField()),
                ('user_name', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('image_url', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
