from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Invoice, InvoiceLine
from track.models import  Track
from customers.serializers import CustomerSerializer
from customers.models import Customer



class InvoiceLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceLine
        # exclude=['invoice_line_id','invoice']
        fields = '__all__'

        
class InvoiceSerializer(serializers.ModelSerializer):
    invoice_lines = serializers.SerializerMethodField()
    customer = CustomerSerializer()

    def get_invoice_lines(self, obj):
        invoice_line_queryset = InvoiceLine.objects.filter(invoice=obj.invoice_id)
        serializer = InvoiceLineSerializer(invoice_line_queryset, many=True)
        return serializer.data


    class Meta:
        model = Invoice
        fields = ['invoice_id', 'customer','invoice_lines', 'invoice_date',
                  'billing_address', 'billing_city', 'billing_state', 
                  'billing_country', 'billing_postal_code', 'total'] 
        
        
    def create(self, validated_data):
        customer_pk = validated_data.pop('customer')
        customer = get_object_or_404(Customer, pk=customer_pk['customer_id'])
        invoice = Invoice.objects.create(customer=customer, **validated_data)
        return invoice
    

    def update(self, instance, validated_data):
        instance.total = validated_data.get('total', instance.total)
        instance.save()
        return instance