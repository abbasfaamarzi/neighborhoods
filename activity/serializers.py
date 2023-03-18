from rest_framework import serializers
from . import models


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Update
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transactions
        fields = '__all__'

class TransactionsHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TransactionsHash
        fields = '__all__'
