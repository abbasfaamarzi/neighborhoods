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

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = models.Transactions.objects.all()
    serializer_class = serializers.TransactionsSerializer
    http_method_names = ['get', 'post', 'delete']
    search_fields = ('authentication')
    ordering_fields = '__all__'

class TransactionsHashViewSet(viewsets.ModelViewSet):
    queryset = models.TransactionsHash.objects.all()
    serializer_class = serializers.TransactionsHashSerializer
    http_method_names = ['get', 'post', 'delete']

    search_fields = ()
    ordering_fields = '__all__'
