from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, ParcelViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'parcels', ParcelViewSet)

urlpatterns = [
    path('', include(router.urls))
]