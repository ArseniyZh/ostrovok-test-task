from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hotels.views import HotelViewSet, CityViewSet

router = DefaultRouter()
router.register(r"hotel", HotelViewSet, basename="hotel")
router.register(r"city", CityViewSet, basename="city")

urlpatterns = [
    path("", include(router.urls)),
]
