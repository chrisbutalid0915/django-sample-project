from django.urls import path
from .views import LocationViewSet


app_name = "locations"

urlpatterns = [
    path("locations", LocationViewSet.as_view({"post": 'create', 'get':'list'})),
    path("locations/<int:pk>", LocationViewSet.as_view({"put": "update", "delete": "destroy"}))
]   