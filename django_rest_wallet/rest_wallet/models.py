from django.conf import settings
from django.db import models
from django.db.models import F

from djmoney.models.fields import MoneyField


class Wallet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='RUB', null=True, default=0, editable=False)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    time_perform = models.DateTimeField(auto_now_add=True)
    value = MoneyField(max_digits=14, decimal_places=2, default_currency='RUB')
    comment = models.CharField(max_length=1023, blank=True, default='')

    def __str__(self):
        return f'{self.wallet} = {self.value}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.pk:
            Wallet.objects.filter(pk=self.wallet_id).update(balance=F('balance') + self.value)
        super(Transaction, self).save()
