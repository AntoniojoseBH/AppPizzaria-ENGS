# Generated by Django 3.2.7 on 2021-11-07 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_orders_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='profile',
        ),
    ]
