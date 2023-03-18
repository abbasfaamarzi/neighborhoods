from django.db import models

# Create your models here.
class Update(models.Model):
    ledgers = models.TextField()
    authentication = models.CharField(max_length=64, primary_key=True)

class Transactions(models.Model):
    transaction_type = models.CharField(max_length=20)
    transaction = models.CharField(max_length=600)
    transaction_signature = models.CharField(max_length=64)

class TransactionsHash(models.Model):
    vb_id = models.CharField(max_length=64)
    trx_hash = models.CharField(max_length=64)
