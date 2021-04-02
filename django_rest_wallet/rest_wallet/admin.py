from django.contrib import admin

from .models import *


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'balance')
    list_filter = ('owner',)
    search_fields = ('name',)


@admin.register(Transaction)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('time_perform', 'wallet', 'value', 'comment')
    # list_filter = ('wallet',)
