from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    proposal_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = serializers.CharField(max_length=36)
    payment_date = serializers.DateTimeField()
