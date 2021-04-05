import pytest
from django.test import TestCase
from mixer.backend.django import mixer

from rest_wallet.models import Wallet, Transaction
from rest_wallet.serializers import (
    WalletSerializer,
    WalletTransactionSerializer, UserTransactionSerializer,
)


@pytest.mark.django_db
class TestWalletSerializer(TestCase):

    def setUp(self) -> None:
        self.wallet = mixer.blend(Wallet)

    def test_serialize_model(self):
        serializer = WalletSerializer(self.wallet)
        assert serializer.data

    def test_serialize_data(self):
        valid_serialized_data = {
            'name': self.wallet.name,
            'balance': self.wallet.balance,
        }
        serializer = WalletSerializer(data=valid_serialized_data)
        assert serializer.is_valid()
        assert serializer.errors == {}


@pytest.mark.django_db
class TestWalletTransactionSerializer(TestCase):

    def setUp(self) -> None:
        self.transaction = mixer.blend(Transaction)

    def test_serialize_model(self):
        serializer = WalletTransactionSerializer(self.transaction)
        assert serializer.data

    def test_serialize_data(self):
        valid_serialized_data = {
            'time_perform': self.transaction.time_perform,
            'value': self.transaction.value,
            'comment': self.transaction.comment
        }
        serializer = WalletTransactionSerializer(data=valid_serialized_data)
        assert serializer.is_valid()
        assert serializer.errors == {}


@pytest.mark.django_db
class TestUserTransactionSerializer(TestCase):

    def setUp(self) -> None:
        self.transaction = mixer.blend(Transaction)

    def test_serialize_model(self):
        serializer = UserTransactionSerializer(self.transaction)
        assert serializer.data

    def test_serialize_data(self):
        valid_serialized_data = {
            'time_perform': self.transaction.time_perform,
            'value': self.transaction.value,
            'comment': self.transaction.comment,
            'wallet': self.transaction.wallet,
        }
        serializer = UserTransactionSerializer(data=valid_serialized_data)
        assert serializer.is_valid()
        assert serializer.errors == {}
