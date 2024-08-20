from django.urls import path , include
from rest_framework.routers import SimpleRouter
from .views import CustomerViewSet
router = SimpleRouter()

router.register('', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]