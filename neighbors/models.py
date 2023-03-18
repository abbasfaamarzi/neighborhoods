from django.db import models

class Update(models.Model):
    ledgers = models.TextField()
    authentication = models.CharField(max_length=64, primary_key=True)
class VolunteerUsers(models.Model):
    text = models.CharField(max_length=1000)
    instagram_url = models.CharField(max_length=1000)
class TrxsHash(models.Model):
    vid_hash = models.CharField(max_length=64)
    trx_hash = models.CharField(max_length=64)
class Profile(models.Model):
    vb = models.IntegerField()
    user_name = models.CharField(max_length=30, unique=True, primary_key=True)
    image_url = models.CharField(max_length=200, blank=True)
class Transactions(models.Model):
    transaction_type = models.CharField(max_length=20)
    transaction = models.CharField(max_length=600)
    transaction_signature = models.CharField(max_length=64)

