# Generated by Django 3.2.7 on 2021-11-07 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='profile',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.profile'),
        ),
    ]