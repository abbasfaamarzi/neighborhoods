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
class TrxsHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TrxsHash
        fields = '__all__'
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'
class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transactions
        fields = '__all__'
