# Generated by Django 3.2.16 on 2023-02-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0046_privateregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrxsHash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_hash', models.CharField(max_length=64)),
                ('trx_hash', models.CharField(max_length=64)),
            ],
        ),
    ]