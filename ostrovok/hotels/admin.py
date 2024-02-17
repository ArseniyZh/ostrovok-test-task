from django.contrib import admin

from hotels.models import City, Hotel


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ("title",)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    fields = ("title", "address", "phone_number", "city",)
