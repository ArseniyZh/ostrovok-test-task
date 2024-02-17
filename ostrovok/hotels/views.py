from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from hotels.models import City, Hotel
from hotels.schemas import hotel_list_params
from hotels.serializers import HotelSerializer, CitySerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @swagger_auto_schema(manual_parameters=hotel_list_params)
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        params = request.GET

        if city_id := params.get("city_id"):
            queryset = queryset.filter(city_id=city_id)
        if from_id := params.get("from_id"):
            queryset = queryset.filter(id__gt=from_id)
        if limit := params.get("limit"):
            queryset = queryset[:int(limit)]

        data = self.serializer_class(queryset, many=True).data
        return Response(data)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
