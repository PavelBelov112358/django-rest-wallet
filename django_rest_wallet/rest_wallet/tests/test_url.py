from django.urls import reverse, resolve


class TestUrls:

    def test_wallet_list_url(self):
        url_name = 'wallet-list'
        path = reverse(url_name)
        assert resolve(path).view_name == url_name

    def test_wallet_detail_url(self):
        url_name = 'wallet-detail'
        path = reverse(url_name, kwargs={'wallet_pk': 1})
        assert resolve(path).view_name == url_name

    def test_wallet_transaction_list_url(self):
        url_name = 'wallet-transaction-list'
        path = reverse(url_name, kwargs={'wallet_pk': 1})
        assert resolve(path).view_name == url_name

    def test_wallet_transaction_detail_url(self):
        url_name = 'wallet-transaction-detail'
        path = reverse(url_name, kwargs={'wallet_pk': 1, 'transaction_pk': 1})
        assert resolve(path).view_name == url_name

    def test_user_transaction_list_url(self):
        url_name = 'user-transaction-list'
        path = reverse(url_name)
        assert resolve(path).view_name == url_name

    def test_user_transaction_detail_url(self):
        url_name = 'user-transaction-detail'
        path = reverse(url_name, kwargs={'transaction_pk': 1})
        assert resolve(path).view_name == url_name
