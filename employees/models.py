from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    title = models.CharField(max_length=30, blank=True, null=True)
    reports_to = models.ForeignKey('self', models.DO_NOTHING, db_column='reports_to', blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    hire_date = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'employee'

