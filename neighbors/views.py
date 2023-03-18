from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
class VolunteerUsersViewSet(viewsets.ModelViewSet):
    queryset = models.VolunteerUsers.objects.all()
    serializer_class = serializers.VolunteerUsersSerializer
    http_method_names = ['get', 'post', 'delete']
    search_fields = ('authentication')
    ordering_fields = '__all__'
class UpdateViewSet(viewsets.ModelViewSet):
    queryset = models.Update.objects.all()
    serializer_class = serializers.UpdateSerializer
    http_method_names = ['get', 'post', 'delete']
    search_fields = ()
    ordering_fields = '__all__'
class TrxsHashViewSet(viewsets.ModelViewSet):
    queryset = models.TrxsHash.objects.all()
    serializer_class = serializers.TrxsHashSerializer
    http_method_names = ['get', 'post', 'delete']

    search_fields = ()
    ordering_fields = '__all__'
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
