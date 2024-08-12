from django.db import models

# Create your models here.


class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    invoice_date = models.DateTimeField()
    billing_address = models.CharField(max_length=70, blank=True, null=True)
    billing_city = models.CharField(max_length=40, blank=True, null=True)
    billing_state = models.CharField(max_length=40, blank=True, null=True)
    billing_country = models.CharField(max_length=40, blank=True, null=True)
    billing_postal_code = models.CharField(max_length=10, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'invoice'


class InvoiceLine(models.Model):
    invoice_line_id = models.IntegerField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    track = models.ForeignKey('Track', models.DO_NOTHING)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'invoice_line'


