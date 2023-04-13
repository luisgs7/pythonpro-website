# Generated by Django 4.1.7 on 2023-04-12 23:28
from datetime import timedelta

from django.db import migrations


def fill_expired_at(Subscription):
    for subscription in Subscription.objects.filter(activated_at__isnull=False).all():
        subscription.expired_at = (subscription.activated_at + timedelta(
            days=subscription.days_of_access
        )).date()
        subscription.save()


def make_expired_at_null(Subscription):
    Subscription.objects.update(expired_at=None)


def _fill_expired_at(apps, schema_editor):
    Subscription = apps.get_model('memberkit', 'Subscription')
    fill_expired_at(Subscription)


def _make_expired_at_null(apps, schema_editor):
    Subscription = apps.get_model('memberkit', 'Subscription')
    make_expired_at_null(Subscription)


class Migration(migrations.Migration):
    dependencies = [
        ('memberkit', '0012_added_subscription_expired_at'),
    ]

    operations = [
        migrations.RunPython(_fill_expired_at, _make_expired_at_null)
    ]
