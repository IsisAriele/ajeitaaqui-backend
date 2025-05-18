# interface_adapters/api/serializers/client_serializer.py

from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    birth_date = serializers.DateField(required=False)
    document = serializers.CharField()
    phone = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.CharField()
    country = serializers.CharField()
    photo = serializers.ImageField(required=False, allow_null=True)
