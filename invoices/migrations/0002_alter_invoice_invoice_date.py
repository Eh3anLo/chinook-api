# Generated by Django 5.0 on 2024-08-19 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
