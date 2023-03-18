# Generated by Django 3.2.16 on 2023-02-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0079_privateregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vb', models.IntegerField()),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
    ]
