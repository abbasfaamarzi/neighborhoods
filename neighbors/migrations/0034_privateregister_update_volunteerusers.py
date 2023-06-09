# Generated by Django 3.2.16 on 2023-01-31 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('neighbors', '0033_auto_20230131_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_hash', models.CharField(max_length=64)),
                ('password_hash', models.CharField(max_length=64)),
                ('lock', models.CharField(max_length=64)),
                ('register_time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('ledgers', models.TextField()),
                ('authentication', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('inestagram_url', models.CharField(max_length=1000)),
            ],
        ),
    ]
