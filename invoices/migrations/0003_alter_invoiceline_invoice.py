# Generated by Django 5.0 on 2024-08-19 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_alter_invoice_invoice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceline',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice'),
        ),
    ]
