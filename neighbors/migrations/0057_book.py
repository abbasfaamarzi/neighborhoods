# Generated by Django 3.2.16 on 2023-02-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0056_election'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('number_of_readers', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
