from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Wallet, Transaction
from .serializers import (
    WalletSerializer,
    WalletTransactionSerializer,
    UserTransactionSerializer
)


class WalletModelViewSet(ModelViewSet):
    serializer_class = WalletSerializer
    lookup_url_kwarg = 'wallet_pk'

    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class WalletTransactionModelViewSet(ModelViewSet):
    serializer_class = WalletTransactionSerializer
    lookup_url_kwarg = 'transaction_pk'

    def get_queryset(self):
        return Transaction.objects.filter(wallet=self.kwargs.get('wallet_pk'))

    def perform_create(self, serializer):
        return serializer.save(wallet_id=self.kwargs.get('wallet_pk'))


class UserTransactionModelViewSet(ReadOnlyModelViewSet):
    serializer_class = UserTransactionSerializer
    lookup_url_kwarg = 'transaction_pk'

    def get_queryset(self):
        return Transaction.objects.filter(wallet__owner=self.request.user)
