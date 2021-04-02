from django.urls import path

from .views import *


urlpatterns = [
    path('wallet/', WalletView.as_view()),
    path('wallet/<int:pk>', WalletView.as_view()),
]
