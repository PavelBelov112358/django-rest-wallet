import pytest
from mixer.backend.django import mixer

from rest_wallet.models import Wallet, Transaction


@pytest.mark.django_db
class TestWalletModel:

    def test_init_wallet_model(self):
        wallet = mixer.blend(Wallet)
        assert wallet.__class__ is Wallet
        assert str(wallet) == wallet.name


@pytest.mark.django_db
class TestTransactionModel:

    def test_init_transaction_model(self):
        transaction = mixer.blend(Transaction)
        assert transaction.__class__ is Transaction
        assert str(transaction) == f'{transaction.wallet} = {transaction.value}'
