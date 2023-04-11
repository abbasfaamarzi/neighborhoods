from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class LedgerUpdate(models.Model):
    authentication_code = models.PositiveIntegerField(
        validators=[MinLengthValidator(6), MaxLengthValidator(6)],
        unique = True
    )
    ledgers = models.JSONField()
    signature_ledgers = models.CharField(max_length=64)

class LedgerVersion(models.Model):
    social_signature = models.CharField(max_length=64)
    period_time = models.FloatField()
class Transaction(models.Model):
    transaction_type = models.CharField(max_length=50)
    transaction_sign = models.TextField(blank=True)
    public_key = models.CharField(max_length=1000)
    sender_id = models.IntegerField(blank=True)
    recipient_id = models.IntegerField(blank=True)
    book_id = models.IntegerField(blank=True)
    propose_price = models.FloatField(blank=True)
    heir_id = models.IntegerField(blank=True)
    neighborhood_fee = models.FloatField(blank=True)
    village_bank_interest = models.FloatField(blank=True)
    coin_price = models.FloatField(blank=True)
    coin_reward = models.FloatField(blank=True)
    mining_period_time = models.FloatField(blank=True)
    book_title_hash = models.CharField(blank=True,max_length=64)
    book_title = models.CharField(blank=True,max_length=64)
    book_txt = models.CharField(blank=True, max_length=64)
    book_cover_url = models.CharField(blank=True, max_length=64)
    book_price = models.FloatField(blank=True)
    owner_id = models.IntegerField(blank=True)
    instagram_url = models.CharField(blank=True)
    wiki_url = models.CharField(blank=True, max_length=64)
    status = models.BooleanField(blank=True)
    publish_time = models.FloatField(blank=True)
    post_id = models.IntegerField(blank=True)
    like = models.BooleanField(blank=True, default=False)
    social_sign = models.CharField(max_length=64, blank=True)