from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('invoices', views.InvoiceViewSet)
router.register('invoice_lines', views.InvoiceLineViewSet)

urlpatterns = [
   path('', include(router.urls)),
]