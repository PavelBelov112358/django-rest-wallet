from rest_framework import serializers

from .models import *


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('id', 'name', 'balance')


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'wallet', 'time_perform', 'value', 'comment')
