from rest_framework.response import Response
from rest_framework import status
from .serializers import SerializerTools
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import LedgerUpdate
from .serializers import LedgerUpdateSerializer
from .filters import LedgerUpdateFilter
import django_filters

class LedgerUpdateViewSet(viewsets.ModelViewSet):
    queryset = LedgerUpdate.objects.all()
    serializer_class = LedgerUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # چک کردن صحت امضا
            signature = serializer.validated_data['signature_ledgers']
            json_data = serializer.validated_data['ledgers']
            auth_code = serializer.validated_data['authentication_code']
            if signature == SerializerTools().Hash(json_data):
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({'detail': 'Invalid signature'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            # چک کردن صحت امضا
            signature = serializer.validated_data['signature_ledgers']
            json_data = serializer.validated_data['ledgers']
            auth_code = serializer.validated_data['authentication_code']
            if signature == SerializerTools().Hash(json_data):
                self.perform_update(serializer)
                return Response(serializer.data)
            else:
                return Response({'detail': 'Invalid signature'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class LedgerUpdateFilteredViewSet(viewsets.ModelViewSet):
    queryset = LedgerUpdate.objects.all()
    serializer_class = LedgerUpdateSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, SearchFilter]
    filterset_class = LedgerUpdateFilter
    search_fields = ['ledgers']
