from rest_framework import serializers


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField()
