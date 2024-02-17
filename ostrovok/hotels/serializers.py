from rest_framework import serializers

from hotels.models import City, Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("id", "title", "address", "phone_number", "city", "created_at", "updated_at",)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "title", "created_at", "updated_at",)
