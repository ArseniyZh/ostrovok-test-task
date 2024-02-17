from drf_yasg import openapi

hotel_list_params = [
    openapi.Parameter(
        "city_id",
        openapi.IN_QUERY,
        type=openapi.TYPE_INTEGER,
        description="Фильтр по городу",
    ),
    openapi.Parameter(
        "from_id",
        openapi.IN_QUERY,
        type=openapi.TYPE_INTEGER,
        description="Все отели id которых больше указанного",
    ),
    openapi.Parameter(
        "limit",
        openapi.IN_QUERY,
        type=openapi.TYPE_INTEGER,
        description="Предел количества отелей в списке",
    ),
]
