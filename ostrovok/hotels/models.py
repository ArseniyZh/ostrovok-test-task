from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import to_python

from common.models import BaseModel


def validate_international_phonenumber(value):
    phone_number = to_python(value)
    if phone_number and not phone_number.is_valid():
        raise ValidationError(
            _("Неверный формат номера телефона"), code="invalid_phone_number"
        )


class City(BaseModel):
    title = models.CharField(max_length=50, help_text="Название города")

    def __str__(self):
        return f"Город #{self.id}: {self.title}"


class Hotel(BaseModel):
    title = models.CharField(max_length=255, help_text="Название отеля")
    address = models.CharField(max_length=255, help_text="Адрес отеля")
    phone_number = PhoneNumberField(
        unique=True, db_index=True, validators=[validate_international_phonenumber], help_text="Контактный номер"
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"Отель #{self.id}: {self.title}"
