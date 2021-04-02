from django.contrib import admin

from .models import *


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'balance')
    list_filter = ('owner',)
    search_fields = ('name',)


@admin.register(Transaction)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_perform', 'value', 'wallet', 'owner', 'comment')
    list_filter = ('wallet',)

    def name(self, object):
        return object

    def owner(self, object):
        return object.wallet.owner

    name.short_description = 'Name'
    owner.short_description = 'Owner'
