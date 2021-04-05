from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    WalletModelViewSet,
    WalletTransactionModelViewSet,
    UserTransactionModelViewSet,
)

wallet_list = WalletModelViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

wallet_detail = WalletModelViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


wallet_transaction_list = WalletTransactionModelViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

wallet_transaction_detail = WalletTransactionModelViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})


user_transaction_list = UserTransactionModelViewSet.as_view({
    'get': 'list',
})

user_transaction_detail = UserTransactionModelViewSet.as_view({
    'get': 'retrieve',
})


urlpatterns = format_suffix_patterns([
    path('wallets/', wallet_list, name='wallet-list'),
    path('wallets/<int:wallet_pk>', wallet_detail, name='wallet-detail'),

    path('wallets/<int:wallet_pk>/transactions/', wallet_transaction_list, name='wallet-transaction-list'),
    path('wallets/<int:wallet_pk>/transactions/<int:transaction_pk>', wallet_transaction_detail,
         name='wallet-transaction-detail'),

    path('transactions/', user_transaction_list, name='user-transaction-list'),
    path('transactions/<int:transaction_pk>', user_transaction_detail, name='user-transaction-detail'),
])
