from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.viewsets import *

from .models import *
from .serializers import *


class WalletView(UpdateAPIView, DestroyAPIView, ListCreateAPIView):
    serializer_class = WalletSerializer

    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        owner = self.request.user
        return serializer.save(owner=owner)


class TransactionView(ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(wallet__owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
