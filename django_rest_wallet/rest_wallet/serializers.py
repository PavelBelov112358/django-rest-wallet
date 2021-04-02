from rest_framework import serializers

from .models import *


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('name', 'balance')


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('time_committal', 'value', 'comment')