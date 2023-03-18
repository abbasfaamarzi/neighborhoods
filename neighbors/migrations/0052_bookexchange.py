# Generated by Django 3.2.16 on 2023-02-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0051_delete_bookexchang'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookExchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=150)),
                ('user_id', models.IntegerField()),
                ('proposed_price', models.FloatField()),
            ],
        ),
    ]
