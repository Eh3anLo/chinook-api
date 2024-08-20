from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InvoiceSerializer, InvoiceLineSerializer
from .models import Invoice, InvoiceLine
# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):
    # queryset = Invoice.objects.select_related('customer').all()
    queryset = Invoice.objects.prefetch_related(
        Prefetch('invoiceline_set', queryset=InvoiceLine.objects.select_related('track')),
    ).select_related('customer')
    serializer_class= InvoiceSerializer


class InvoiceLineViewSet(viewsets.ModelViewSet):
    queryset = InvoiceLine.objects.select_related('track','invoice')
    serializer_class = InvoiceLineSerializer