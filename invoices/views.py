from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InvoiceSerializer, InvoiceLineSerializer
from .models import Invoice, InvoiceLine
# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.select_related('customer').all()
    serializer_class= InvoiceSerializer


class InvoiceLineViewSet(viewsets.ModelViewSet):
    queryset = InvoiceLine.objects.select_related('track','invoice').all()
    serializer_class = InvoiceLineSerializer