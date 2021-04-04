from rest_framework import serializers

from .models import *


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        exclude = ('owner',)


class WalletTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        exclude = ('wallet',)


class UserTransactionSerializer(serializers.ModelSerializer):
    wallet = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'
