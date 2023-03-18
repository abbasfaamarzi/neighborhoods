from django.db import models
class Table_Version(models.Model):
    version_number = models.IntegerField()
    social_signature = models.CharField(max_length=64)
    period_time = models.IntegerField()
class User(models.Model):
    wallet_id = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

class PublicInfo(models.Model):
    user_name = models.CharField(max_length=40)
    profile_image = models.CharField(max_length=300)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

class PrivateInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    heir_id = models.CharField(max_length=64, default="village bank")
    amount = models.FloatField(default=0)
    lock = models.CharField(max_length=64)
    status = models.BooleanField(default=True)

class MyLedger(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=40)
    image_url = models.CharField(max_length=300)
    wallet_id = models.CharField(max_length=64)
    follower = models.ForeignKey('Followers', related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='following_user', on_delete=models.CASCADE)
    amount = models.ForeignKey(PrivateInfo, on_delete=models.CASCADE)
    heir_id = models.ForeignKey(PrivateInfo, related_name='heir', on_delete=models.CASCADE)
    auto_login = models.BooleanField(default=False)
    login_time = models.DateTimeField(auto_now_add=True)

class Followers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='followers')

class PublicAccount(models.Model):
    account_name = models.CharField(max_length=30)
    amount = models.FloatField(default=0.0)
    ceo = models.OneToOneField(User, on_delete=models.CASCADE)

class BookLibrary(models.Model):
    book_title_hash = models.CharField(max_length=64, unique=True)
    book_title = models.CharField(max_length=100)
    book_txt = models.CharField(max_length=64)
    book_cover_url = models.CharField(max_length=300)
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    instagram_url = models.CharField(max_length=300)
    wiki_url = models.CharField(max_length=300)
    for_self = models.BooleanField()
    publish_time = models.DateTimeField(auto_now=True)
class BookOwner(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    book_id = models.OneToOneField(BookLibrary, on_delete=models.CASCADE)
class Election(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idea_text = models.CharField(max_length=400, blank=True)
    neighborhood_fee = models.FloatField(default=0.0001, blank=True)
    village_bank_interest = models.FloatField(default=0.0, blank=True)
    coin_price = models.FloatField(default=0.0, blank=True)
    coin_reward = models.FloatField(default=6.25, blank=True)
    mining_period_time = models.FloatField(default=600.0, blank=True)
    election_period = models.IntegerField(blank=True)
    like = models.ForeignKey('Like', on_delete=models.CASCADE)

class Like(models.Model):
    election_id = models.OneToOneField(Election, on_delete=models.CASCADE)
    like_by_user_id = models.OneToOneField(User, on_delete=models.CASCADE)
class Key_Chain(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE)
    new_key = models.IntegerField()
