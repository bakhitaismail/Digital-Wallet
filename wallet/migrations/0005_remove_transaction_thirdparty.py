# Generated by Django 4.0.6 on 2022-08-25 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_transaction_origin_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='thirdparty',
        ),
    ]