# Generated by Django 3.1.7 on 2021-04-01 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_wallet', '0003_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='time_committal',
            new_name='time_perform',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=1023),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
