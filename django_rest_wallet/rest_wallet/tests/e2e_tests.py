import json
from datetime import datetime

import pytest

from django.conf import settings
from django.test import TestCase

from rest_framework.test import APIClient

from mixer.backend.django import mixer

from rest_wallet.models import Wallet, Transaction


@pytest.mark.django_db
class TestWalletEndpoints(TestCase):

    def setUp(self) -> None:
        self.user = mixer.blend(settings.AUTH_USER_MODEL)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.endpoint = '/api/v1/wallets/'

    def test_list(self):
        number = 3
        mixer.cycle(number).blend(Wallet, owner=self.user)
        response = self.client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == number

    def test_create(self):
        created_json = {'name': 'test'}
        expected_json = {
            'id': 1,
            'balance': '%.2f' % 0,
            'balance_currency': 'RUB'
        }
        expected_json.update(created_json)
        response = self.client.post(self.endpoint, data=created_json, format='json')

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json

    def test_retrieve(self):
        wallet = mixer.blend(Wallet, owner=self.user)
        expected_json = {
            'id': wallet.id,
            'name': wallet.name,
            'balance': '%.2f' % 0,
            'balance_currency': 'RUB'
        }
        url = f'{self.endpoint}{wallet.id}'
        response = self.client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_update(self):
        wallet = mixer.blend(Wallet, owner=self.user)
        updated_json = {'name': 'test'}
        expected_json = {
            'id': wallet.id,
            'balance': '%.2f' % 0,
            'balance_currency': 'RUB'
        }
        expected_json.update(updated_json)
        url = f'{self.endpoint}{wallet.id}'
        response = self.client.put(url, data=updated_json, format='json')

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_partial_update(self):
        wallet = mixer.blend(Wallet, owner=self.user)
        updated_json = {'name': 'test'}
        expected_json = {
            'id': wallet.id,
            'balance': '%.2f' % 0,
            'balance_currency': 'RUB'
        }
        expected_json.update(updated_json)
        url = f'{self.endpoint}{wallet.id}'
        response = self.client.patch(url, data=updated_json, format='json')

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_destroy(self):
        wallet = mixer.blend(Wallet, owner=self.user)
        url = f'{self.endpoint}{wallet.id}'
        response = self.client.delete(url)

        assert response.status_code == 204
        assert not Wallet.objects.all()


@pytest.mark.django_db
class TestWalletTransactionEndpoints(TestCase):

    def setUp(self) -> None:
        self.user = mixer.blend(settings.AUTH_USER_MODEL)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.wallet = mixer.blend(Wallet, owner=self.user)
        self.endpoint = f'/api/v1/wallets/{self.wallet.id}/transactions/'

    def test_list(self):
        number = 3
        mixer.cycle(number).blend(Transaction, wallet=self.wallet)
        response = self.client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == number

    def test_create(self):
        created_json = {'value': 100, 'comment': 'test'}
        expected_json = {
            'id': 1,
            'value': '%.2f' % 100,
            'value_currency': 'RUB',
            'time_perform':  str(datetime.now()),
            'comment': 'test'
        }
        response = self.client.post(self.endpoint, data=created_json, format='json')
        response_json = json.loads(response.content)

        assert response.status_code == 201

        for key, item in expected_json.items():
            if key == 'time_perform':
                assert response_json.get(key) > item
                continue
            assert response_json.get(key) == item

        assert str(Wallet.objects.get(pk=self.wallet.id).balance) == '100.00 руб.'

    def test_retrieve(self):
        transaction = mixer.blend(Transaction, wallet=self.wallet)

        url = f'{self.endpoint}{transaction.id}'
        response = self.client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content).get('id') == transaction.id

    def test_destroy(self):
        transaction = mixer.blend(Transaction, wallet=self.wallet)
        url = f'{self.endpoint}{transaction.id}'
        response = self.client.delete(url)

        assert response.status_code == 204
        assert not Transaction.objects.all()


@pytest.mark.django_db
class TestUserTransactionEndpoints(TestCase):

    def setUp(self) -> None:
        self.user = mixer.blend(settings.AUTH_USER_MODEL)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.wallet = mixer.blend(Wallet, owner=self.user)
        self.transactions = mixer.cycle(2).blend(Transaction, wallet=self.wallet)
        print(type(self.transactions))
        self.endpoint = f'/api/v1/transactions/'

    def test_list(self):
        response = self.client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_retrieve(self):
        transaction = self.transactions[0]
        url = f'{self.endpoint}{transaction.id}'
        response = self.client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content).get('id') == transaction.id
        assert json.loads(response.content).get('wallet') == str(self.wallet)
