# Generated by Django 5.1.1 on 2024-10-27 15:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_alter_transaction_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
