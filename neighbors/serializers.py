from rest_framework import serializers
from .models import LedgerUpdate
import hashlib
import json
class SerializerTools:
    def Hash(self, data):
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
class LedgerUpdateSerializer(serializers.ModelSerializer):
    signature_ledgers = serializers.SerializerMethodField()
    ser = SerializerTools()

    def get_signature_ledgers(self, obj):
        # دریافت فایل JSON از شیء مدل
        json_data = obj.ledgers

        # ایجاد signature_ledgers با استفاده از تابع hash_json
        signature = self.ser.Hash(json_data)

        return signature

    def validate(self, data):
        # دریافت فایل JSON و هش‌شده‌ی آن
        json_data = data.get('ledgers')
        json_signature = data.get('signature_ledgers')

        # بررسی همانندی هش‌ها
        if self.ser.Hash(json_data) != json_signature:
            raise serializers.ValidationError("Invalid signature!")

        return data

    class Meta:
        model = LedgerUpdate
        fields = ['authentication_code', 'ledgers', 'signature_ledgers']
from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'





