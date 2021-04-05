import pytest
from mixer.backend.django import mixer

from django.conf import settings
from django.test import RequestFactory, TestCase
from django.urls import reverse

from rest_wallet.models import Wallet, Transaction

from rest_wallet.urls import (
    wallet_list,
    wallet_detail,
    wallet_transaction_list,
    wallet_transaction_detail,
    user_transaction_list,
    user_transaction_detail,
)


@pytest.mark.django_db
class TestViews(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = mixer.blend(settings.AUTH_USER_MODEL)
        wallet = mixer.blend(Wallet, owner=self.user)
        transaction = mixer.blend(Transaction, wallet=wallet)

    def test_wallet_list_view_set(self):
        path = reverse('wallet-list')
        request = self.factory.get(path)
        request.user = self.user
        view = wallet_list
        response = view(request)
        assert response.status_code == 200

    def test_wallet_detail_view_set(self):
        path = reverse('wallet-detail', kwargs={'wallet_pk': 1})
        request = self.factory.get(path)
        request.user = self.user
        view = wallet_detail
        response = view(request, wallet_pk=1)
        assert response.status_code == 200

    def test_wallet_transaction_list_view_set(self):
        path = reverse('wallet-transaction-list', kwargs={'wallet_pk': 1})
        request = self.factory.get(path)
        request.user = self.user
        view = wallet_transaction_list
        response = view(request, wallet_pk=1)
        assert response.status_code == 200

    def test_wallet_transaction_detail_view_set(self):
        path = reverse('wallet-transaction-detail', kwargs={'wallet_pk': 1, 'transaction_pk': 1})
        request = self.factory.get(path)
        request.user = self.user
        view = wallet_transaction_detail
        response = view(request, wallet_pk=1, transaction_pk=1)
        assert response.status_code == 200

    def test_user_transaction_list_view_set(self):
        path = reverse('user-transaction-list')
        request = self.factory.get(path)
        request.user = self.user
        view = user_transaction_list
        response = view(request)
        assert response.status_code == 200

    def test_user_transaction_detail_view_set(self):
        path = reverse('user-transaction-detail', kwargs={'transaction_pk': 1})
        request = self.factory.get(path)
        request.user = self.user
        view = user_transaction_detail
        response = view(request, transaction_pk=1)
        assert response.status_code == 200
