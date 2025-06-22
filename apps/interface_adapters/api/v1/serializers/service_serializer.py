from rest_framework import serializers


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=1000, required=False, allow_blank=True)
