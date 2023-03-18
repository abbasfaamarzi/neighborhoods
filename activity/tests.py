from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class UpdateViewSet(viewsets.ModelViewSet):
    queryset = models.Update.objects.all()
    serializer_class = serializers.UpdateSerializer
    http_method_names = ['get', 'post', 'delete']
    search_fields = ()
    ordering_fields = '__all__'


class VolunteerUsersViewSet(viewsets.ModelViewSet):
    queryset = models.VolunteerUsers.objects.all()
    serializer_class = serializers.VolunteerUsersSerializer
    http_method_names = ['get', 'post', 'delete']
    search_fields = ('authentication')
    ordering_fields = '__all__'


class PrivateRegisterViewSet(viewsets.ModelViewSet):
    queryset = models.PrivateRegister.objects.all()
    serializer_class = serializers.PrivateRegisterSerializer
    http_method_names = ['get', 'post', 'delete']

    search_fields = ()
    ordering_fields = '__all__'


class TrxsHashViewSet(viewsets.ModelViewSet):
    queryset = models.TrxsHash.objects.all()
    serializer_class = serializers.TrxsHashSerializer
    http_method_names = ['get', 'post', 'delete']

    search_fields = ()
    ordering_fields = '__all__'


class CoinTransactionViewSet(viewsets.ModelViewSet):
    queryset = models.CoinTransaction.objects.all()
    serializer_class = serializers.CoinTransactionSerializer
    http_method_names = ['get', 'post', 'delete']

    search_fields = ()
    ordering_fields = '__all__'


class BookTransactionViewSet(viewsets.ModelViewSet):
    queryset = models.BookTransaction.objects.all()
    serializer_class = serializers.BookTransactionSerializer
    http_method_names = ['get', 'post', 'delete']


class BookExchangeViewSet(viewsets.ModelViewSet):
    queryset = models.BookExchange.objects.all()
    serializer_class = serializers.BookExchangeSerializer
    http_method_names = ['get', 'post', 'delete']

    search_fields = ()
    ordering_fields = '__all__'


class BookPublishViewSet(viewsets.ModelViewSet):
    queryset = models.BookPublish.objects.all()
    serializer_class = serializers.BookPublishSerializer
    http_method_names = ['get', 'post', 'delete']

    search_fields = ()
    ordering_fields = '__all__'


class ElectionViewSet(viewsets.ModelViewSet):
    queryset = models.Election.objects.all()
    serializer_class = serializers.ElectionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ()
    ordering_fields = '__all__'


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = models.Transactions.objects.all()
    serializer_class = serializers.TransactionsSerializer
    http_method_names = ['get', 'post', 'delete']
    search_fields = ('authentication')
    ordering_fields = '__all__'

from django.db import models

class Update(models.Model):
    ledgers = models.TextField()
    authentication = models.CharField(max_length=64, primary_key=True)

class VolunteerUsers(models.Model):
    text = models.CharField(max_length=1000)
    instagram_url = models.CharField(max_length=1000)

class PrivateRegister(models.Model):
    vid_hash = models.CharField(max_length=64, primary_key=True)
    password_hash = models.CharField(max_length=64)
    lock = models.CharField(max_length=64)
    register_time =models.FloatField()

class TrxsHash(models.Model):
    vid_hash = models.CharField(max_length=64)
    trx_hash = models.CharField(max_length=64)

class CoinTransaction(models.Model):
    trx = models.CharField(max_length=2000)

class BookTransaction(models.Model):
    trx = models.CharField(max_length=2000)

class BookExchange(models.Model):
    book_title = models.CharField(max_length=150)
    user_id = models.IntegerField()
    proposed_price = models.FloatField()

class BookPublish(models.Model):
    book_publisher_id = models.IntegerField()
    book_title = models.CharField(max_length=30)
    book_text = models.CharField(max_length=500)
    book_cover_url = models.CharField(max_length=500)
    last_price = models.FloatField(blank=True, default=0.0)
    owner_id = models.IntegerField(blank=True, default=-1)
    instagram_url = models.CharField(max_length=500, blank=True)
    wiki_url = models.CharField(max_length=500)
    status = models.CharField(max_length=10)

class Election(models.Model):
    user_name = models.CharField(max_length=50)
    idea_type = models.CharField(max_length=100)
    text = models.CharField(max_length=500, blank=True)
    idea_url = models.CharField(max_length=200)
    idea_data = models.TextField()
    like = models.IntegerField(default=0)
class Profile(models.Model):
    vb = models.IntegerField()
    user_name = models.CharField(max_length=30, unique=True, primary_key=True)
    image_url = models.CharField(max_length=200, blank=True)

class Transactions(models.Model):
    transaction_type = models.CharField(max_length=20)
    transaction = models.CharField(max_length=600)
    transaction_signature = models.CharField(max_length=64)

class Notifications(models.Model):
    first_vb = models.IntegerField()
    second_vb = models.IntegerField(blank=True)
    notification_data = models.CharField(max_length=700)

from rest_framework import serializers
from . import models


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Update
        fields = '__all__'

class VolunteerUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VolunteerUsers
        fields = '__all__'

class PrivateRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrivateRegister
        fields = '__all__'

class TrxsHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TrxsHash
        fields = '__all__'

class CoinTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoinTransaction
        fields = '__all__'

class BookTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookTransaction
        fields = '__all__'
class BookExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookExchange
        fields = '__all__'

class BookPublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookPublish
        fields = '__all__'
class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Election
        fields = '__all__'

    def update(self, instance, validated_data):
        previous_like = instance.like
        new_reaction = list(validated_data.items())
        print(new_reaction)
        obj = super().update(instance, validated_data)
        if new_reaction[5][1] % 2 ==0:
            instance.like = previous_like + 1
        else:
            instance.like = previous_like - 1
        obj.save()
        return obj
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transactions
        fields = '__all__'
from django.urls import path
from rest_framework.routers import DefaultRouter
from neighbors import views


router = DefaultRouter()
router.register('update', views.UpdateViewSet)
router.register('volunteer_users', views.VolunteerUsersViewSet)
router.register('private_register', views.PrivateRegisterViewSet)
router.register('trxs_hash', views.TrxsHashViewSet)
router.register('coin_transaction', views.CoinTransactionViewSet)
router.register('book_transaction', views.BookTransactionViewSet)
router.register('book_exchange', views.BookExchangeViewSet)
router.register('book_publish', views.BookPublishViewSet)
router.register('election', views.ElectionViewSet)
router.register('profile', views.ProfileViewSet)
router.register('transactions', views.TransactionsViewSet)

urlpatterns = []

urlpatterns += router.urls
